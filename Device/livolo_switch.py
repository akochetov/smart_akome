import livolo as Livolo

from device_signal import Signal
from device_signal import DeviceSignalFactory

#deserialize signal json passed as parameter
liv_pin = DeviceSignalFactory.pinFromArgs()
signal = DeviceSignalFactory.signalFromArgs()

ptrn_len = len(signal.Pattern)
i = 0

if (ptrn_len>=2):#there are actual codes to send - initiate wiringPi and livolo
    Livolo.setupGPIO()

while i<ptrn_len:
    remoteID = signal.Pattern[i]
    code = signal.Pattern[i+1]
    i=i+2
    print("Sending to remote ID - " + str(remoteID) + ", code - " + str(code))
    Livolo.sendButton(liv_pin,remoteID,code)
