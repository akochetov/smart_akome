from AKO.GPIO._IrTxDevice import *
import sys
import json

from device_signal import Signal

print(sys.argv[1])
signal = Signal(**json.loads(sys.argv[1]))
irtx = IrTxDevice()
pattern = list(signal.Pattern)

key = ""
for char_code in pattern:
    key = key + chr(char_code)
print(key)
irtx.SendOnce(key, "/home/pi/lircd.conf")

