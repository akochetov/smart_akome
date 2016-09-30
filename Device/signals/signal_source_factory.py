from inputdevice_signal_source import InputDeviceSignalSource
from queue_signal_source import QueueSignalSource
from ir_signal_source import IrSignalSource

sources = {'inputdevice':InputDeviceSignalSource,'queue':QueueSignalSource,'ir':IrSignalSource}

class SignalSourceFactory():
    @staticmethod
    def createInstance(typ):
        return sources[typ]()
