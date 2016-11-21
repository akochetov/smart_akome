import io
import json
import datetime
import time

import subprocess

import threading

from model.device import Device
from model.device import DeviceFactory
from model.device_signal import Signal

def log(message):
    print "%s: %s" % (str(datetime.datetime.now()),message)

class ProcessorPathBuilder():   
    @staticmethod
    def getPath(device):
        return "sudo python -u ./processors/"+device.Processor+".py '"+DeviceFactory.toJson(device)+"' >./logs/"+device.Processor+"_"+str(device.ID)+".log 2>&1 &"

class DeviceThread(threading.Thread):
    def __init__(self, app_path):
        threading.Thread.__init__(self)
        self._app_path = app_path
        self._process = None
    
    def run(self):
        # Create the subprocess, redirect the standard output into a pipe
        self._process = subprocess.Popen(self._app_path,
                    shell=True,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)

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

    def __init__(self):
        self.UpdateDevices()
        self.UpdateThreads()
    
    def UpdateDevices(self):
        del self._devices[:]
        with open('../Web/appserver/config/default.json', 'r') as f:
            ln = f.read()
            devices = json.loads(ln)
            for device in devices:                
                self._devices.append(Device(**device))
    
    def UpdateThreads(self):     
        self.KillThreads()
        for device in self._devices:
            if (not device.Processor == ''):
                app = ProcessorPathBuilder.getPath(device)
                log("Starting device: ID - %d, app - %s" % (device.ID,app))
                thread = DeviceThread(app)
                thread.start()
                self._threads.append(thread)
            
    def KillThreads(self):
        for thread in self._threads:
            thread.stop()
        del self._threads[:]

    def Destroy(self):
        self.KillThreads()
        
dispatcher = DeviceDispatcher()

print('Devices started. To exit press Ctrl+C\r\n')

while True:
    time.sleep(1)

dispatcher.Destroy()



