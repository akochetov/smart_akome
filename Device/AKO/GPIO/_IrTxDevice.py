from lircsend import LircSend

#----------------------------------------------------
#IrTxDevice class. Transmitts signals to IR receivers    
class IrTxDevice():
    _lirc = None

    #-----------------------------------------------
    #Constructor. Creates lirc instance
    def __init__(self):
        self._lirc = LircSend.create_local()
    #----------------------------------
    #Call Lirc's SEND_ONCE command
    def SendOnce(self, key, remote, repeat = 1):
        self._lirc.send_once(key,remote,repeat)
