from AKO.GPIO._IrTxDevice import *
import sys
import json

from device_signal import Signal

print(sys.argv[1])
signal = Signal(**json.loads(sys.argv[1]))
irtx = IrTxDevice()
irtx.SendOnce(signal.Pattern, "/home/pi/lircd.conf")

