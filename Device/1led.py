from AKO.GPIO._OutputDevice import *
import time

led_pin = 23

led = OutputDevice(led_pin)

for i in range (0,100):
    led.On()
    time.sleep(0.5)
    led.Off()
