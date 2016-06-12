import threading
import time as Time

#setup modes
MODE_UNKNOWN = -1
BOARD        = 10
BCM          = 11
ERIAL       = 40
SPI          = 41
I2C          = 42
PWM          = 43

#constants
IN = 1
OUT = 1

HIGH = 1
LOW  = 0

PUD_OFF  = 0
PUD_DOWN = 1
PUD_UP   = 2

NO_EDGE      = 0
RISING  = 1
FALLING = 2
BOTH    = 3

#test message
message = [1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,0,1,0,0]
m_index = 0

#thread for tests
class DetectThread(threading.Thread):
    def __init__(self, pin, callback):
        threading.Thread.__init__(self)
        self._callback = callback
        self._pin = pin

    def run(self):
        Time.sleep(1)
        global message
        for i in range(0,len(message)):
            self._callback(self._pin)
            tm = Time.clock()
            while ((Time.clock()-tm)<0.0007):
                2*2
            
#functions
def setmode(mode):
    print("GPIO setmode. mode: "+str(mode))

def setup(gpio, direction, pull_up_down=PUD_UP):
    print("GPIO setup. gpio: "+str(gpio)+", direction: "+str(direction)+", pud: "+str(pull_up_down))

def cleanup():
    print("GPIO cleanup")

def input(channel):
    global m_index
    global message
    
    result = abs(message[m_index]-1)
    #print("GPIO channel input. channel: " + str(channel) + ", input: " +str(message[m_index]))
    
    if (m_index<len(message)-1):
        m_index += 1
    else:
        m_index = 0
        
    return result

def output(channel, signal):
    print("GPIO channel output. channel: " + str(channel) + ", output: " + str(signal))

def add_event_detect(channel, edge, callback, bouncetime=0):
    thread = DetectThread(channel, callback)
    thread.start()

def remove_event_detect(channel):
    print("GPIO event removed for channel: "+str(channel))
    
