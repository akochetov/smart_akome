from livolo_signal_destination import LivoloSignalDestination
from speakers_signal_destination import SpeakersSignalDestination
from queue_signal_destination import QueueSignalDestination

signals = {'livolo':LivoloSignalDestination,'speakers':SpeakersSignalDestination, 'queue':QueueSignalDestination}

class SignalDestinationFactory():
    @staticmethod
    def createInstance(typ):
        return signals[typ]()
