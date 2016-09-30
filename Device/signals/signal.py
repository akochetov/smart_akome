from abc import abstractmethod
import datetime

class SignalSource():
    _on_signal_received = None

    def log(self,message):
        print "%s: %s" % (str(datetime.datetime.now()),message)
    
    @abstractmethod
    def init(self,device):
        raise NotImplementedError("subclass must override init()")
    @abstractmethod
    def start(self):
        raise NotImplementedError("subclass must override start()")
    @abstractmethod
    def stop(self):
        raise NotImplementedError("subclass must override stop()")
    @abstractmethod
    def input(self):
        raise NotImplementedError("subclass must override input()")
    
    def on_signal_received(self,signal):
        if (not self._on_signal_received == None):
            self._on_signal_received(signal)

    def set_signal_received(self,on_signal_received):
        self._on_signal_received = on_signal_received


class SignalDestination():
    def log(self,message):
        print "%s: %s" % (str(datetime.datetime.now()),message)
    
    @abstractmethod
    def init(self,device):
        raise NotImplementedError("subclass must override init()")
    @abstractmethod
    def start(self):
        raise NotImplementedError("subclass must override start()")
    @abstractmethod
    def stop(self):
        raise NotImplementedError("subclass must override stop()")
    def send(self,signal):
        raise NotImplementedError("subclass must override send()")
    
