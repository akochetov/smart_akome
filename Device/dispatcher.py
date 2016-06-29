import io
import json

import subprocess

import threading

from device import Device
from device_signal import Signal

class DeviceThread(threading.Thread):
    def __init__(self, app_path):
        threading.Thread.__init__(self)
        self._app_path = app_path
        self._process = None
        self._data_callback = None
    
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
                print("input received: "+line)
                
                if (not self._data_callback is None):
                    self._data_callback(line)
            except:
                break
        
    def stop(self):
        if (self._process != None):        
            self._process.kill()          
            self._process = None

    def set_data_callback(self, func):
        self._data_callback = func

class DeviceDispatcher():
    _devices = []
    _threads = []

    def __init__(self):
        self.UpdateDevices()
        self.UpdateThreads()
    
    def UpdateDevices(self):
        del self._devices[:]
        with open('../Web/appserver/devices.json', 'r') as f:
            ln = f.read()
            devices = json.loads(ln)
            for device in devices:                
                self._devices.append(Device(**device))

    def InputFromDevice(self, data):
        signal = Signal(**json.loads(data))

        for device in self._devices:
            if device.ID == signal.DeviceID:
                print("Starting signal app: ID - "+str(device.ID)+" , app path - "+device.App+" "+str(device.Pin)+" '"+data+"'")
                subprocess.Popen(device.App+" "+str(device.Pin)+" '"+data+"'",shell=True)

    def UpdateThreads(self):
        self.KillThreads()
        for device in self._devices:            
            if not device.App == '' and (device.CommunicationMethod == Device.CommunicationMethod_Send or device.CommunicationMethod == Device.CommunicationMethod_Both):
                print("Starting device: ID - "+str(device.ID)+", app path - "+device.App)
                thread = DeviceThread(device.App)
                thread.set_data_callback(self.InputFromDevice)
                thread.start()
                self._threads.append(thread)
            
    def KillThreads(self):
        for thread in self._threads:
            thread.stop()
        del self._threads[:]

    def Destroy(self):
        self.KillThreads()
        
dispatcher = DeviceDispatcher()

input('Devices started. To exit press any key\r\n')

dispatcher.Destroy()



