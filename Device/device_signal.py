class Signal():
    ID = 0
    Name = ""
    Icon = ""
    SignalDirection = 0
    Pattern = []
    DeviceID = 0

    def __init__(self,ID,Name,DeviceID,Icon='',Pattern=[],SignalDirection=0):
        self.ID = ID
        self.Name = Name
        self.Icon = Icon
        self.SignalDirection = SignalDirection
        self.DeviceID = DeviceID
        self.Pattern = Pattern
