import RPi.GPIO as GPIO
import time as Time
import threading
import atexit

from AKO.GPIO._InputDevice import *

#----------------------------------------------------
#IrRxMesageThread. Derived from Thread, permanently
#runs and checks if there was a pause after last signal recieved. 
class IrRxMessageThread(threading.Thread):
    def __init__(self, IrRxDevice):
        threading.Thread.__init__(self)
        self._device = IrRxDevice
        self._exiting = False

    def run(self):
        while not self._exiting:
            Time.sleep(self._device.message_timeout)
            if (self._device.IsMessageTimedOut()):
                self._device.TriggerMessageReceived()

    def Stop(self):
        #signal to the thread func to exit
        self._exiting = True
                    
    def __del__(self):
        #stop thread in destructor
        self.Stop()

#----------------------------------------------------
#IrRxDevice class. Receives signals from IR receivers    
class IrRxDevice(InputDevice):
    #------------------------------------------
    #constants
    message_timeout = 0.1  #in seconds. if there is no signal received during 10ms - treat transmission as finished
    lastirrx = 0            #last signal receiving time
    bitrate = 0.0007         #signal bitrate. Seems to be 0.0007 for IR. Change if needed
    buffer = []             #internal buffer to store incoming signal time spans
    last_state = 0          #last signal state (high or low)
    MessageReceived = None #event for message receiving. None by default

    #-----------------------------------------------
    #Constructor. Starts message received thread and registers callbacks
    def __init__(self, pin, pullup=True):
        InputDevice.__init__(self,pin=pin,pullup=pullup)

        #start thread to detect message received and trigger events
        self.messagethread = IrRxMessageThread(self)
        self.messagethread.start()

        #get ready to receive data
        self.ClearMessage()

        #register callback for GPIO
        GPIO.add_event_detect(pin,GPIO.BOTH, callback=self.IrRxSignalReceived)
    #-----------------------------------------------
    #Returns if message receiving is timed out
    def IsMessageTimedOut(self):
        return len(self.buffer) and self.Diff()>self.message_timeout
    #-----------------------------------------------
    #Message receiving thread calls this method.
    #Method then decodes received message and clears it
    def TriggerMessageReceived(self):
        self.DecodeMessage()
        self.ClearMessage()
        
    #-----------------------------------------------
    #Raise message events
    def RaiseMessageReceived(self, message):
        if (len(message) and not self.MessageReceived == None):            
            self.MessageReceived(message)
    #-----------------------------------------------
    #Decode received message and raise events
    def DecodeMessage(self):
        print("buffer ("+str(len(self.buffer))+": "+ str(self.buffer))
                
        #join subsequent highs and lows
        i = 0
        l = len(self.buffer)-1
        while (i < l):
            if (self.Sign(self.buffer[i])==self.Sign(self.buffer[i+1])):
                self.buffer[i+1] += self.buffer[i]
                self.buffer.pop(i)
                l-=1
            else:
                i+=1

        print("buffer ("+str(len(self.buffer))+": "+ str(self.buffer))

        #now convert signal chunks into 0s and 1s with transmission bitrate
        result = []    
        for item in self.buffer:
            n = int(round(abs(item)/self.bitrate))

            if (n>=4):#new message has started - raise event with previous message contents and start new message
                if (len(result)):
                    self.RaiseMessageReceived(result)
                result.clear()#start new message

            #convert signal to 0 or 1 depending if it was high or low
            for i in range(0,n):
                if (item>0):
                    result.append(1)#high was received, add 1
                else:
                    result.append(0)#low was recieved, add 0

        #raise event for final message received
        if (len(result)):
            self.RaiseMessageReceived(result)
            
    #------------------------------------------
    #Clear all buffers and get ready to next transmission
    def ClearMessage(self):
        self.buffer = []
        self.last_state = 5
        self.lastirrx = 0
           
    #------------------------------------------
    #Add received signal to message bufer
    def RegisterSignal(self, channel):
        if (self.lastirrx == 0):
            diff = self.bitrate                 #if this is a first signal in message - add bitrate as timespan
        else:
            diff = self.Diff()                  #otherise add time since previous signal
       
        self.lastirrx = self.Time()
        
        state = GPIO.input(channel)             #read state if this is High or Low
        self.buffer.append(self.StateSign(state)*diff) #add time span since last high or low to buffer, change sign depending on current high or low
        self.last_state = state
    #------------------------------------------
    #Event handler for GPIO signal event
    def IrRxSignalReceived(self,channel):      
        self.RegisterSignal(channel)
    #------------------------------------------
    #Stop method to stop message receiving thread
    def Stop(self):
        self.messagethread.Stop()
    #------------------------------------------
    #Destructor
    def __del__(self):
        self.Stop()
    #-----------------------------------------------
    #Utility method to detect precise time
    def Time(self):
        return Time.clock()
    #-----------------------------------------------
    #Utility method to detect time diff from last sample
    def Diff(self):
        return abs(Time.clock()-self.lastirrx);
    #-----------------------------------------------
    #Utility method to detect sign of an int
    def Sign(self, x):
        return int(x>0)
    #------------------------------------------
    #Utility method. Retuns -1 if signalis high, 1 if signal is low
    def StateSign(self, state):
        if (state == GPIO.HIGH):
            return -1
        else:
            return 1
