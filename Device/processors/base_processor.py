from abc import abstractmethod

import sys
sys.path.append(sys.path[0]+'/..')

from model.device import DeviceFactory
from model.device_signal import Signal

from signals.signal import SignalDestination
from signals.signal import SignalSource
from signals.signal_destination_factory import SignalDestinationFactory
from signals.signal_source_factory import SignalSourceFactory

import datetime

#----------------------------------------------------
class BaseProcessor:
    _device = None
    _commandSource = None
    _signalSource = None
    _signalDest = None

    def __init__(self):
        self._device = DeviceFactory.fromArgs()
        
        if (not self._device.SignalSource == ''):
            self._signalSource = SignalSourceFactory.createInstance(self._device.SignalSource)
            self._signalSource.set_signal_received(self.on_signal_received)
            
        if (not self._device.SignalDestination == ''):
            self._signalDest = SignalDestinationFactory.createInstance(self._device.SignalDestination)     

    def log(self,message):
        print "%s: %s" % (str(datetime.datetime.now()),message)
        sys.stdout.flush()

    def start(self):       
        if (not self._signalSource == None):
            self._signalSource.init(self._device)
            self._signalSource.start()

        if (not self._signalDest == None):
            self._signalDest.init(self._device)
            self._signalDest.start()
        
    def stop(self):
        if (not self._signalSource == None):
            self._signalSource.stop()
        if (not self._signalDest == None):
            self._signalDest.stop()

    def sendSignal(self,signal):
        if (not self._signalDest == None):
            self._signalDest.send(signal)
            
    def on_signal_received(self, signal):
        found = False

        for sig in self._device.Signals:
            if (signal.Name == sig.Name or signal.Pattern == sig.Pattern):
                self.sendSignal(sig)
                found = True
                self.log("Signal found and sent: "+str(sig.ID)+", "+sig.Name)
            
        if (not found):
            self.log("Signal not found: "+str(signal.ID)+", "+signal.Name)

#----------------------------------------------------
            

