import RPi.GPIO as GPIO
import time as Time
import threading
import atexit
import math

from AKO.GPIO._OutputDevice import *

#----------------------------------------------------
#IrTxDevice class. Transmitts signals to IR receivers    
class IrTxDevice(OutputDevice):
    #------------------------------------------
    #constants
    bitrate = 0.002          #signal bitrate. Seems to be 0.0007 for IR. Change if needed
    lastirtx = 0            #time of last transmission

    #-----------------------------------------------
    #Constructor. Starts message received thread and registers callbacks
    def __init__(self, pin):
        OutputDevice.__init__(self,pin=pin)

    #-----------------------------------------------
    #Transmits bytes
    def SendMessage(self, tx_bytes):
        for bt in tx_bytes:
            for i in range(0,8):
                n = math.pow(2,i)

                if (bt & int(n)):
                    self.On()
                else:
                    self.Off()
                    
                self.lastirtx = self.Time()
                self.Sleep()

        self.lastirtx = 0
        self.Off()
    #-----------------------------------------------
    #Utility method to detect precise time
    def Sleep(self):
        while (self.Diff()<self.bitrate):
            2*2#Time.sleep(self.bitrate/10)
    #-----------------------------------------------
    #Utility method to detect precise time
    def Time(self):
        return Time.time()+Time.clock()
    #-----------------------------------------------
    #Utility method to detect time diff from last sample
    def Diff(self):
        return abs(self.Time()-self.lastirtx);
