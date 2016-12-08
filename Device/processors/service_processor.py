import threading
import datetime
import time
import math

import pika

import sys
sys.path.append(sys.path[0]+'/..')

from model.appserver_request import AppServerRequest
from model.appserver_response import AppServerResponse
from model.appserver_request import AppServerRequestFactory
from model.appserver_response import AppServerResponseFactory

from model.device import DeviceFactory
from model.device import Device

from util.backwards_reader import BackwardsReader

logs_folder = "../logs/"

#----------------------------------------------------
class ServiceProcessor():
    queue = ''
    
    _connection = None
    _channel = None
    _thread = None
    
    def __init__(self):
        if len(sys.argv) < 2:
            raise ValueError('parameter must be relative queue path (without "smart_akome:")')

        self.queue = sys.argv[1];   
 
    def log(self,message):
        print "%s: %s" % (str(datetime.datetime.now()),message)
        sys.stdout.flush()

    def start(self):
        self.initConnection()
        self._thread = threading.Thread(target=self.run)
        self._thread.start()

    def stop(self):
        if (not self._connection == None):
            self.closeConnection()
            self._thread.join()

    def run(self):
        while (not self._connection == None):
            try:
                self._connection.process_data_events(1)
            except:
                pass

    #-------------------------------------------------        

    def closeConnection(self):
        self._connection.close()
        self._connection = None
        self._channel = None

    def initConnection(self):
        self.stop()
        
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()
        
        self._channel.queue_declare(queue='smart_akome:'+self.queue, durable = False, exclusive = False, auto_delete = False)
        self._channel.basic_consume(self.callback, queue='smart_akome:'+self.queue, no_ack=True)
        self.log("Source queue has been set up: smart_akome:"+self.queue)

    def callback(self, ch, method, properties, body):
        self.signalReceived(body.decode())

    def signalReceived(self,request):        
        req = AppServerRequestFactory.fromJson(request)
        
        device = DeviceFactory.fromJson(req.requestBody)
        
        fname = logs_folder+device.Processor+"_"+str(device.ID)+".log"

        res = '';
        lines = 0.0

        log = BackwardsReader(fname, 4096)

        try:
            #skip starting log entries till necessary page starts
            for i in range(0,req.pageIndex*req.pageSize):
                if (log.readline()):
                    lines=lines+1
            #now read next page to string
            for i in range(req.pageIndex*req.pageSize,(req.pageIndex+1)*req.pageSize):
                s = log.readline()
                if (s):
                    lines=lines+1
                    res = res + s
            #read rest of log
            while (log.readline()):
                lines=lines+1

        except:
            log.close()
            
        response = AppServerResponse()
        response.pagesNumber = math.ceil(lines/req.pageSize)
        response.pageSize = req.pageSize
        response.responseBody = res.split('\n')[:-1]
       
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.basic_publish(exchange='', routing_key=req.responseQueue, body=AppServerResponseFactory.toJson(response))
        connection.close()
        

#----------------------------------------------------
            

service = ServiceProcessor()
service.start()

service.log("Service processor started")

while True:
    time.sleep(1)

service.stop()
service.log("Service processor stopped")


