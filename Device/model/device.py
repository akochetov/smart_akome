import sys
import json

from device_signal import Signal

class Device():
    CommunicationMethod_Send = 1
    CommunicationMethod_Receive = 2
    CommunicationMethod_Both = 3
    
    ID = 0
    Name = ''
    Processor = ''
    Icon = ''
    SignalSource = ''
    SignalDestination = ''
    SignalSourceID = 0
    SignalDestinationID = 0
    CommunicationMethod = 0
    Signals = []
    Settings = []
    
    def __init__(self,ID,Name='',Processor='',Icon='',Signals=[],Settings=[],CommunicationMethod=0,SignalSource = '',SignalDestination = '',SignalSourceID = 0,SignalDestinationID = 0):
        self.ID = ID
        self.Name = Name
        self.Processor = Processor
        self.Icon = Icon
        self.CommunicationMethod = CommunicationMethod

        #read signals json
        self.Signals = []
        self.Settings = []
        for signal in Signals:
            self.Signals.append(Signal(**signal))

        self.Settings = Settings

        #read signals setup
        self.SignalSource = SignalSource
        self.SignalDestination = SignalDestination
        self.SignalSourceID = SignalSourceID
        self.SignalDestinationID = SignalDestinationID

    def getSourceID(self):
        if (self.SignalSourceID == 0):
            return self.ID
        return self.SignalSourceID

    def getDestinationID(self):
        if (self.SignalDestinationID == 0):
            return self.ID
        return self.SignalDestinationID

class DeviceFactory():
    @staticmethod
    def fromJson(jsonString):
        return Device(**json.loads(jsonString))
    @staticmethod
    def toJson(device):
        signals = "[";
        for signal in device.Signals:
            if len(signals) > 1:
                signals = signals+","
            signals = signals+json.dumps(signal.__dict__) 
        signals = signals+"]";
        sig = device.Signals
        device.Signals = []
        result = json.dumps(device.__dict__)
        result = result.replace("\"Signals\": []","\"Signals\": "+signals)
        print result
        return result
        device.Signals = sig
    @staticmethod
    def fromArgs():
        if len(sys.argv) < 2:
            raise ValueError('parameter must be json put in single qoutes')
        return DeviceFactory.fromJson(sys.argv[1])
