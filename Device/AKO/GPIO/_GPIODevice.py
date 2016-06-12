import RPi.GPIO as GPIO

#GPIODevice class. Base class responsible for GPIO init and cleanup
class GPIODevice():
  
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
    def __del__():
        GPIO.cleanup()
