import time as Time
import threading
import atexit
import AKO/AKO.GPIO._IrRxDevice as GPIO

#IrRx event handler
def sign(x):
    return int(x>0)

def t():
    sm=0
    with open("msg.txt", "a") as file:
        for item in message:

            file.write(str(sm+abs(item*100000))+"\t"+str(sign(item))+"\n")
            file.write(str(sm+abs(item*100000))+"\t"+str(sign(-item))+"\n")
            
            sm+=abs(item*100000)

def IrMessageReceived(message):
    with open("msg.txt", "a") as file:
        for item in message:
            file.write(str(item)+" ")
        file.write("\n")
    print("result ("+str(len(message))+"): "+str(message))
#end of IrRx event handlers

#Main program

irrxpin = 24

irrx = GPIO.IrRxDevice(irrxpin)
irrx.MessageReceived = IrMessageReceived
  
try:
    input("Ir Rx is ready. Press Enter to exit.\n")
except:
    s=0

irrx.Stop()

