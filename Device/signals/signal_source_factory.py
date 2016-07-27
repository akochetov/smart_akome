from inputdevice_signal_source import InputDeviceSignalSource
from queue_signal_source import QueueSignalSource

sources = {'inputdevice':InputDeviceSignalSource,'queue':QueueSignalSource}

class SignalSourceFactory():
    @staticmethod
    def createInstance(typ):
        return sources[typ]()
