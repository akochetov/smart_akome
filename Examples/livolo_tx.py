import livolo as Livolo
import time

Livolo.setupGPIO()

pin = 23
#remoteID = 1, 4, 16, 64, 256, 1024, 4096, 16384
#remoteID = 2043
remoteID = 1
#code1 = 8
code1 = 120
#code0 = 42
code0 = 106 

for i in range(0, 10):
    print('Turning lights ON...')
    Livolo.sendButton(pin, remoteID, code1)
    time.sleep(1)
    print('Turning lights OFF...')
    Livolo.sendButton(pin, remoteID, code0)
    time.sleep(1)

