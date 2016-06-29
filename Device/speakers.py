from AKO.GPIO._IrTxDevice import *

from device_signal import Signal
from device_signal import DeviceSignalFactory

#deserialize signal json passed as parameter
signal = DeviceSignalFactory.signalFromArgs()

irtx = IrTxDevice()
pattern = list(signal.Pattern)

key = ""
for char_code in pattern:
    key = key + chr(char_code)
print(key)
irtx.SendOnce(key, "/home/pi/lircd.conf")

