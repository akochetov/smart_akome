import RPi.GPIO as GPIO
from AKO.GPIO._GPIODevice import *

#InputDevice class for buttons ans switches
class InputDevice(GPIODevice):

    signalReceived = None   #signal received event. None by default
    bouncetime = 0
  
    def __init__(self, pin, pullup=True, bouncetime = -666):
        GPIODevice.__init__(self)
        self.pin = pin
        self.bouncetime = bouncetime
        
        if (pullup):
            GPIO.setup(self.pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        else:
            GPIO.setup(self.pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        self.subscribeToGPIO()

    def subscribeToGPIO(self):
        GPIO.remove_event_detect(self.pin)
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=self.on_message_received, bouncetime=self.bouncetime)

    def setBounceTime(bouncetime):
        self.bouncetime = bouncetime
        self.subscribeToGPIO()

    def input(self):
        return GPIO.input(self.pin)

    #---------------------------------------
    #Internal event handler for GPIO input
    def on_message_received(self, channel):
        if (not self.signalReceived==None):
            self.signalReceived(GPIO.input(self.pin))
