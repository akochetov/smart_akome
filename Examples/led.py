from gpiozero import *
from time import *

ledpin= 13

print("Now led at pin "+str(ledpin)+" will blink. To stop press Ctrl+C")

led = OutputDevice(ledpin)
try:
    while True:
        led.off()
        sleep(0.05)
        led.on()
        sleep(0.05)
except KeyboardInterrupt:
    led.off();
    print("Led is now off")

led.close()
