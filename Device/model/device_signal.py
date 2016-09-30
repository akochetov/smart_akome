import sys
import json

class Signal():
    ID = 0
    Name = ""
    Icon = ""
    SignalDirection = 0
    SignalDestinationID = 0
    Pattern = []
    DeviceID = 0

    def __init__(self,ID,Name='',DeviceID = 0,Icon='',Pattern=[],SignalDirection=0,SignalDestinationID=0):
        self.ID = ID
        self.Name = Name
        self.Icon = Icon
        self.SignalDirection = SignalDirection
        self.SignalDestinationID = SignalDestinationID
        self.DeviceID = DeviceID
        self.Pattern = Pattern

class DeviceSignalFactory():
    @staticmethod
    def fromJson(jsonString):
        return Signal(**json.loads(jsonString))
    @staticmethod
    def toJson(signal):
        return json.dumps(signal.__dict__)
    @staticmethod
    def fromArgs():
        if len(sys.argv) < 3:
            raise ValueError('second parameter must be json put in single qoutes')
        return DeviceSignalFactory.signalFromJson(sys.argv[2])
    @staticmethod
    def pinFromArgs():
        if len(sys.argv) < 2 or not sys.argv[1].isdigit():
            raise ValueError('first parameter must be int - pin number')
        return int(sys.argv[1])
