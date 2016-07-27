from signal import SignalSource

from AKO.GPIO._InputDevice import *
from model.device_signal import Signal

class InputDeviceSignalSource(SignalSource):
    _device = None
    _on_signal_received = None
    _input = None
    
    def init(self,device):
        self._device = device

    def start(self):
        self._input = InputDevice(self._device.Settings["pin"],True)
        self._input.signalReceived = self.signalReceived
        
    def stop(self):
        pass

    def input(self):
        return _input.input()

    def signalReceived(self,value):
        self.on_signal_received(Signal(ID=0,Pattern=[value]))
