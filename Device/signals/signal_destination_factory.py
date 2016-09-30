from livolo_signal_destination import LivoloSignalDestination
from ir_signal_destination import IrSignalDestination
from queue_signal_destination import QueueSignalDestination

signals = {'livolo':LivoloSignalDestination,'ir':IrSignalDestination, 'queue':QueueSignalDestination}

class SignalDestinationFactory():
    @staticmethod
    def createInstance(typ):
        return signals[typ]()
