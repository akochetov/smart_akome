import IRRxTx as irrxtx
import time as Time
from signal import SignalDestination

class IrSignalDestination(SignalDestination):  
    _device = None

    def init(self,device):
        self._device = device

    def start(self):
        irrxtx.setupGPIO()

    def stop(self):
        pass
    
    def send(self,signal):
        pin = self._device.Settings["pin"]
        pattern = list(signal.Pattern)

        for code in pattern:
            irrxtx.irTransmit(pin,code);
            self.log("Sending ir: "+str(code))
            Time.sleep(1)
        


