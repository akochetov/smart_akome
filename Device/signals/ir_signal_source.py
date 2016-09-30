import datetime
import time
import threading

import IRRxTx as irrxtx
from signal import SignalSource

from model.device_signal import Signal

#----------------------------------------------------
#thread to receive async data 
class DataThread(threading.Thread):
    _exiting = False
    _pin = None
    _source = None
    
    def __init__(self, pin, source):
        threading.Thread.__init__(self)
        self._pin = pin
        self._source = source
        self.daemon = False

    def run(self):
             
        while not self._exiting:
            time.sleep(0.5)
            result = irrxtx.irReceive(self._pin)
            
            if (result):
                self._source.log("Data received: "+str(result))
                self._source.signalReceived(result)

    def Stop(self):
        #signal to the thread func to exit
        self._exiting = True
                            
    def __del__(self):
        #stop thread in destructor
        self.Stop()

class IrSignalSource(SignalSource):
    _device = None
    _on_signal_received = None
    _datathread = None
    
    def init(self,device):
        self._device = device
        
        #start wiringPi
        irrxtx.setupGPIO()

        pin = self._device.Settings["pin"]
        irrxtx.irEnableReceive(pin)
        
        self._datathread = DataThread(pin,self)

    def start(self):
        self._datathread.start()
        
    def stop(self):
        self._datathread.Stop()
        pin = self._device.Settings["pin"]
        irrxtx.irDisableReceive(pin)

    def signalReceived(self,value):
        self.on_signal_received(Signal(ID=0,Pattern=[value]))
