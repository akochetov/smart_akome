import time as Time
import threading
import atexit
import AKO.GPIO._IrTxDevice as GPIO

#Main program

irtxpin = 4

irtx = GPIO.IrTxDevice(irtxpin)
irtx.SendMessage([15,2,3])
    
try:      
    input("Press Enter to exit.\n")
except:
    s=0


