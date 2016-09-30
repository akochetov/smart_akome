import datetime
import time
import threading

import IRRxTx as irrxtx

send_pin = 25
receive_pin = 24

#----------------------------------------------------
#thread to receive async data 
class DataThread(threading.Thread):
    _exiting = False
    _pin = None
    
    def __init__(self, pin):
        threading.Thread.__init__(self)
        self._pin = pin

    def run(self):
        irrxtx.irEnableReceive(self._pin)
                
        while not self._exiting:
            time.sleep(0.5)
            result = irrxtx.irReceive(self._pin)
            if (result):
                print("Data received: "+str(result))

        irrxtx.irDisableReceive(self._pin)
        
    def Stop(self):
        #signal to the thread func to exit
        self._exiting = True
                    
    def __del__(self):
        #stop thread in destructor
        self.Stop()


irrxtx.setupGPIO()

datathread = DataThread(receive_pin)
datathread.start();

#irrxtx.irTransmit(send_pin,4278249232);

while True:
    time.sleep(1)    

