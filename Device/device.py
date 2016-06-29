class Device():
    CommunicationMethod_Send = 1
    CommunicationMethod_Receive = 2
    CommunicationMethod_Both = 3
    
    ID = 0
    Name = ''
    App = ''
    Icon = ''
    Pin = 0
    CommunicationMethod = 0
    
    def __init__(self,ID,Name,App='',Icon='',Pin = 0,Signals=[],CommunicationMethod=0):
        self.ID = ID
        self.Name = Name
        self.App = App
        self.Icon = Icon
        self.Pin = Pin
        self.CommunicationMethod = CommunicationMethod
