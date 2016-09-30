import pika
import json
import pickle
import threading

from signal import SignalDestination
from model.device_signal import DeviceSignalFactory

#----------------------------------------------------
#Signal sending class for RabbitMQ queue
class QueueSignalDestination(SignalDestination):
    _device = None
    _connection = None
    _channel = None

    def init(self, device):
        self._device = device       

    def start(self):
        self.initConnection()

    def stop(self):
        if (not self._connection == None):
            self.closeConnection()

    def send(self, signal):
        #by default send signal to destination ID specified in device
        dest_id = self._device.getDestinationID()

        #if destination is specified per signal - use it
        if (signal.SignalDestinationID):
            dest_id=signal.SignalDestinationID
            
        self._channel.basic_publish(exchange='', routing_key='smart_akome:'+str(dest_id), body=DeviceSignalFactory.toJson(signal))

    #-------------------------------------------------
    #derived class specific methods

    def closeConnection(self):   
        self._connection.close()
        self._connection = None
        self._channel = None
        self.log("Destination queue has been shot down: smart_akome:"+str(self._device.getDestinationID()))

    def initConnection(self):
        self.stop()

        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()

        self._channel.queue_declare(queue='smart_akome:'+str(self._device.getDestinationID()), durable = False, exclusive = False, auto_delete = False)
        self.log("Destination queue has been set up: smart_akome:"+str(self._device.getDestinationID()))
         

#----------------------------------------------------
            

