import time as Time
import threading
import atexit
import AKO.GPIO._IrTxDevice as GPIO

#Main program

irtxpin = 17

irtx = GPIO.IrTxDevice(irtxpin)
#0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0 1 0 1 0 1 0 1 0 1 1 0 1 0 1 0 1 0 1 1 0 1 1 0 1 1 0 1 0 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0
"""
191 - 1 1 1 1 1 1 0 1
170 - 0 1 0 1 0 1 0 1
085 - 1 0 1 0 1 0 1 0
219 - 1 1 0 1 1 0 1 1
106 - 0 1 0 1 0 1 1 0
219 - 1 1 0 1 1 0 1 1
170 - 0 1 0 1 0 1 0 1
170 - 0 1 0 1 0 1 0 1
182 - 0 1 1 0 1 1 0 1
109 - 1 0 1 1 0 1 1 0
027 - 1 1 0 1 1 0 0 0
"""
#irtx.SendMessage([000,000,191,170,85,219,106,219,170,170,182,109,27])
irtx.SendMessage([255,0,255])

"""
try:      
    input("Press Enter to exit.\n")
except:
    s=0
"""
