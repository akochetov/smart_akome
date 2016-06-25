from AKO.GPIO._OutputDevice import *
import time

led_pin = 4
beep_pin = 25

color_pins = [23, 22, 27]

led = OutputDevice(led_pin)
beep = OutputDevice(beep_pin)

color_leds = []
for i in range(0,3):
    color_leds.append(OutputDevice(color_pins[i]))

#turn led on
led.On()

for clr_led in color_leds:
    clr_led.On()
    time.sleep(1)

for i in range(1,500):
    beep.On()
    time.sleep(0.001)
    beep.Off()
    time.sleep(0.001)

#turn led off
led.Off()

for clr_led in color_leds:
    clr_led.Off()    

