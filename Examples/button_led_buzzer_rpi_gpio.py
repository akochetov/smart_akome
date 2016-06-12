import time as Time
import threading
import atexit

from AKO.GPIO._InputDevice import *
from AKO.GPIO._OutputDevice import *

#Buzzer beep thread
class BeepThread(threading.Thread):
    def run(self):
        global buzzleron
        buzzleron = True
        while buzzleron:
            buzzer.on();
            Time.sleep(0.001)
            buzzer.off();
            Time.sleep(0.001)
#end of Buzzer beep thread
#Button event handler
def ButtonHandler(state):
    global buzzleron
    if (buzzleron or state):
        print("Button was released at "+str(Time.time()))
        buzzleron = False
        led.off()
    else:
        print("Button was pressed at "+str(Time.time()))
        led.on()
        beepthread = BeepThread()
        beepthread.start()
#end of Button event handlers


#IrRx event handler
def IrMessageReceived(message):
    print("message "+message);
#end of IrRx event handlers

#Main program

buttonpin = 21
ledpin = 13
buzzerpin = 5
irrxpin = 4

GPIO.setmode(GPIO.BCM)

button = InputDevice(buttonpin)
led = OutputDevice(ledpin)
buzzer = OutputDevice(buzzerpin)
   
def _cleanup():
    led.off()

atexit.register(_cleanup)

bounce = 10
buzzleron = False

try:
    input("Please make sure:\n"+
          "button is connected to pin "+str(buttonpin)+
          "\nled is connected to pin "+str(ledpin)+
          "\nbuzzer is connected to pin "+str(buzzerpin)+
          "\nand then press Enter\n")
except:
    s=0

button.SignalReceived = ButtonHandler;

try:      
    input("Press the button to turn led on/off. Press Enter to exit.\n")
except:
    s=0
