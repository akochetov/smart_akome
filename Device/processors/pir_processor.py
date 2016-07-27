import datetime
import time
import threading

from base_processor import BaseProcessor

from AKO.GPIO._InputDevice import *

import sys
sys.path.append('..')

from signals.signal_destination_factory import SignalDestinationFactory
from model.device import Device

class PIRProcessor(BaseProcessor):
    _signalDestList = []
    _light_sensor = None

    def getLightDevice(self,deviceID):
        device = Device(ID=deviceID)
        device.Settings["pin"] = self._device.Settings["light_sensor_pin"]
        return device

    def start(self):       
        for light in self._device.Settings["light_devices"]:
            dest = SignalDestinationFactory.createInstance(self._device.SignalDestination)
            dest.init(self.getLightDevice(light))
            dest.start()
            self._signalDestList.append(dest)

        #light sensor instance
        self._light_sensor = InputDevice(self._device.Settings["light_sensor_pin"], False)

    def stop(self):
        for dest in self._signalDestList:
            dest.stop()
    
    def on_signal_received(self, signal):
        print("Signal received: " +str(signal.Pattern))
        global last_trigger
        global light_thread

        pir_value = signal.Pattern[0]
      
        if not pir_value:#if it is a fall from high to low - no further actions
            return

        #record time when motion was detected
        last_trigger = time.time()
        
        light_value = self.get_light()
        print("Motion detected at: "+str(datetime.datetime.now())+". Light sensor value: "+str(light_value))
        if (light_value == 1):#1 means no light, 0 - light is on.
            light_thread.On()

    def on(self):
        for dest in self._signalDestList:
            dest.send(self._device.Settings["command_on"])

    def off(self):
        for dest in self._signalDestList:
            dest.send(self._device.Settings["command_off"])

    def get_tries(self):
        return self._device.Settings["tries"]

    def get_timeout(self):
        return self._device.Settings["timeout"]
        
    def get_light(self):
        return self._light_sensor.input()

#----------------------------------------------------
#thread to turn the light on or off
class LightTriggerThread():
    _exiting = False
    _off = 1
    _thread = None
    _pir = None

    def __init__(self,pir):
        self._pir = pir

    def run(self):
        global last_trigger

        self._exiting = False

        for i in range(1,self._pir.get_tries()+1):
            if (self._exiting):
                print("Exiting light trigger thread at: "+str(datetime.datetime.now()))
                break;
            
            last_trigger = time.time()
            
            if (self._off == 1):
                print("Turning the light off. Try #"+str(i)+" at: "+str(datetime.datetime.now()))
                self._pir.off()
            else:
                print("Turning the light on. Try #"+str(i)+" at: "+str(datetime.datetime.now()))
                self._pir.on()

            #sleep and check if the light is now on
            time.sleep(0.5)
            
            if (self._pir.get_light() == self._off):
                print("Operation successfull at: "+str(datetime.datetime.now()))
                break
            else:
                print("Operation failed at: "+str(datetime.datetime.now()))
        
    def On(self):
        self.Stop()
        self._off = 0
        self.Start()
        
    def Off(self):
        self.Stop()
        self._off = 1
        self.Start()

    def Start(self):
        self._thread = threading.Thread(target = self.run)
        self._thread.start()

    def Stop(self):
        if (self._thread == None or not self._thread.is_alive()):
            return
        #signal to the thread func to exit
        self._exiting = True
        self._thread.join()
                    
    def __del__(self):
        #stop thread in destructor
        self.Stop()

#----------------------------------------------------
#thread to check ligh off timeout and turn the light if needed 
class TimeoutThread(threading.Thread):
    _exiting = False
    _pir = None
    
    def __init__(self, pir):
        threading.Thread.__init__(self)
        self._pir = pir

    def run(self):
        global last_trigger
        global light_thread
                
        while not self._exiting:
            time.sleep(1)

            if (time.time()-last_trigger > self._pir.get_timeout()):
                light_value = self._pir.get_light()
                if (light_value == 0):#1 means no light, 0 - light is on.                    
                    light_thread.Off()

    def Stop(self):
        #signal to the thread func to exit
        self._exiting = True
                    
    def __del__(self):
        #stop thread in destructor
        self.Stop()


#----------------------------------------

#last time the light was turned on. current time by default
last_trigger = time.time()

pir = PIRProcessor()
pir.start()

#create light thread
light_thread = LightTriggerThread(pir)

#start timeout thread
timeout_thread = TimeoutThread(pir)
timeout_thread.start()

print("Processor started for device: "+str(pir._device.ID))

while True:
    time.sleep(1)    

print("Stopping PIR processor...")
timeout_thread.Stop()
pir.stop()
print("PIR processor stopped")



