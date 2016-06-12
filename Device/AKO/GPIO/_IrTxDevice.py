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
    bitrate = 0.0007          #signal bitrate. Seems to be 0.0007 for IR. Change if needed

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
            Time.sleep(self.bitrate)
