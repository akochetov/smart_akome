from AKO.GPIO._IrTxDevice import *
from signal import SignalDestination

class SpeakersSignalDestination(SignalDestination):  
    _device = None
    _irtx = None

    def init(self,device):
        self._device = device

    def start(self):
        self._irtx = IrTxDevice()

    def stop(self):
        pass
    
    def send(self,signal):
        pin = 0#todo. has to be parsed from self._device
        pattern = list(signal.Pattern)

        key = ""
        for char_code in pattern:
            key = key + chr(char_code)

        print("Sending to speakers, key: "+key)
        self._irtx.SendOnce(key, "/home/pi/lircd.conf")


