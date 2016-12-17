import datetime
import time
import threading
import subprocess
import sys
import os
import json
import Queue

from base_processor import BaseProcessor

from model.device import Device
from model.device import DeviceFactory
from model.device_signal import Signal

from signals.signal_source_factory import SignalSourceFactory

processors_folder = "./"
logs_folder = "../logs/"
configs_folder = "../../Web/appserver/"

callback_queue = Queue.Queue()

def log(message):
    print "%s: %s" % (str(datetime.datetime.now()),message)

class ProcessorPathBuilder():   
    @staticmethod
    def getPath(device):
        return "sudo python -u "+processors_folder+device.Processor+".py '"+DeviceFactory.toJson(device)+"' >> "+logs_folder+device.Processor+"_"+str(device.ID)+".log 2>&1 &"

class DeviceStarter():
    @staticmethod
    def startDevice(app_path):
        return subprocess.Popen(app_path,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

class DeviceThread(threading.Thread):
    def __init__(self, app_path):
        threading.Thread.__init__(self)
        #self.daemon = True
        self._app_path = app_path
        self._process = None
    
    def run(self):
        # Create the subprocess, redirect the standard output into a pipe
        self._process = DeviceStarter.startDevice(self._app_path)

        while True:
            try:
                # Read one line of output
                if self._process == None:
                    break
                data = self._process.stdout.readline()
                if not data:
                    break
                line = data.decode('utf-8').rstrip()
                log(line)                
            except:
                break
        
    def stop(self):
        if (self._process != None):        
            self._process.kill()          
            self._process = None

class DeviceDispatcher():
    _devices = []
    _threads = []    

    def start(self,path):
        if (not os.path.isfile(path)):
            log("Configuration file was not found. Ignoring signal. Path: "+path)
            return
        
        log("Loading devices. Path: "+path)        
        self.updateDevices(path)
        self.updateThreads()
        log("Devices loaded")

    def stop(self):
        self.killThreads()
    
    def updateDevices(self,path):
        del self._devices[:]
        with open(path, 'r') as f:#'../Web/appserver/config/default.json'
            ln = f.read()
            devices = json.loads(ln)
            for device in devices:                
                self._devices.append(Device(**device))
    
    def updateThreads(self):     
        self.killThreads()
        for device in self._devices:
            if (not device.Processor == ''):
                app = ProcessorPathBuilder.getPath(device)
                log("Starting device: ID - %d, app - %s" % (device.ID,app))
                thread = DeviceThread(app)
                thread.start()
                self._threads.append(thread)
            
    def killThreads(self):
        log("Shutting devices down")
        for thread in self._threads:
            thread.stop()
        del self._threads[:]
        log("Devices shot down successfully")

class DispatchingProcessor(BaseProcessor):
    _dispatcher = None

    def __init__(self):
        self._dispatcher = DeviceDispatcher()
                
        if len(sys.argv) < 2:
            raise ValueError('parameter must be dispatcher virtual device ID')

        self._device = Device(sys.argv[1],SignalSource='queue')        
        
        if (not self._device.SignalSource == ''):
            self._signalSource = SignalSourceFactory.createInstance(self._device.SignalSource)
            self._signalSource.set_signal_received(self.on_signal_received)
 
    def start(self):
        BaseProcessor.start(self)
        self.log("Dispatching processor started")
 
    def stop(self):
        BaseProcessor.stop(self)
        self._dispatcher.stop()
    
    def on_signal_received(self, signal):
        #we expect input signal to contain a path to a config
        path = configs_folder+''.join(chr(i) for i in signal.Pattern)

        callback_queue.put((self._dispatcher.start,[path]))
        

dispatcher = DispatchingProcessor()
dispatcher.start()

while True:
    func, args = callback_queue.get()
    func(*args)

dispatcher.log("Stopping dispatching processor...")
dispatcher.stop()
dispatcher.log("Dispatching processor stopped")



