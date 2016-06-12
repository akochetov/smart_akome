import RPi.GPIO as GPIO
from AKO.GPIO._GPIODevice import *

#OutputDevice class for leds and buzzers
class OutputDevice():
    
    def __init__(self, pin):
        GPIODevice.__init__(self)
        self.pin = pin
        GPIO.setup(self.pin,GPIO.OUT)

    def On(self):
        if (self.pin>0):
            GPIO.output(self.pin,GPIO.HIGH)

    def Off(self):
        if (self.pin>0):
            GPIO.output(self.pin,GPIO.LOW)
