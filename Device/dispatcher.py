import io
import json

import subprocess

import threading

class Device():
    ID = 0
    Name = ''
    App = ''
    
    def __init__(self,ID,Name,App):
        self.ID = ID
        self.Name = Name
        self.App = App

class Signal():
    ID = 0
    Name = ""
    SignalDirection = 0
    Pattern = []
    DeviceID = 0
    Device = ""

class DeviceThread(threading.Thread):
    def __init__(self, app_path):
        threading.Thread.__init__(self)
        self._app_path = app_path
        self._process = None
    
    def run(self):
        # Create the subprocess, redirect the standard output into a pipe
        self._process = subprocess.Popen(self._app_path,
                    shell=False,
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
            except:
                break
        
    def stop(self):
        if (self._process != None):        
            self._process.kill()          
            self._process = None
            

def ReadDevices():
    result = []
    with open('devices.json', 'r') as f:
        ln = f.read()
        devices = json.loads(ln)
        for device in devices:
            result.append(Device(**device))
    return result
            
devices = ReadDevices()

threads = []
for device in devices:
    print("device: ID - "+str(device.ID)+", app path - "+device.App)
    thread = DeviceThread(device.App)
    thread.start()
    threads.append(thread)

input(' [*] Waiting for messages. To exit press any key\r\n')

for thread in threads:
    thread.stop()

