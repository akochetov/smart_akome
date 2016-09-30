import livolo as Livolo

from signal import SignalDestination

class LivoloSignalDestination(SignalDestination):  
    _device = None

    def init(self,device):
        self._device = device

    def start(self):
        Livolo.setupGPIO()
        self.log("Livolo GPIO will be setup for device pin: "+str(self._device.Settings["pin"]))

    def stop(self):
        pass
    
    def send(self,signal):
        pin = self._device.Settings["pin"]

        ptrn_len = len(signal.Pattern)
        i = 0

        while i<ptrn_len:
            remoteID = signal.Pattern[i]
            code = signal.Pattern[i+1]
            i=i+2
            self.log("Sending to remote ID - " + str(remoteID) + ", code - " + str(code))
            Livolo.sendButton(pin,remoteID,code)
            self.log("Done")
