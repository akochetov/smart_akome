import RPi.GPIO as GPIO
from AKO.GPIO._GPIODevice import *

#InputDevice class for buttons ans switches
class InputDevice(GPIODevice):

    SignalReceived = None   #signal received event. None by default
    bouncetime = 0
  
    def __init__(self, pin, pullup=True, bouncetime = -666):
        GPIODevice.__init__(self)
        self.pin = pin
        self.bouncetime = bouncetime
        
        if (pullup):
            GPIO.setup(self.pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        else:
            GPIO.setup(self.pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        self.SubscribeToGPIO()

    def SubscribeToGPIO(self):
        GPIO.remove_event_detect(self.pin)
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=self.OnMessageReceived, bouncetime=self.bouncetime)

    def SetBounceTime(bouncetime):
        self.bouncetime = bouncetime
        self.SubscribeToGPIO()

    #---------------------------------------
    #Internal event handler for GPIO input
    def OnMessageReceived(self, channel):
        if (not self.SignalReceived==None):
            self.SignalReceived(GPIO.input(self.pin))
