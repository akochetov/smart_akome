import pika
import json
import pickle
import threading

from signal import SignalSource
from model.device_signal import DeviceSignalFactory

#----------------------------------------------------
#Signal source for RabbitMQ queue
class QueueSignalSource(SignalSource):
    _device = None
    _connection = None
    _thread = None
    _last_signal = None
    
    def init(self, device):
        self._device = device
        self.initConnection()

    def start(self):
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
    #derived class specific methods

    def closeConnection(self):
        self._connection.close()
        self._connection = None
        self._channel = None

    def initConnection(self):
        self.stop()
        
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()
        
        self._channel.queue_declare(queue='smart_akome:'+str(self._device.getSourceID()), durable = False, exclusive = False, auto_delete = False)
        self._channel.basic_consume(self.callback, queue='smart_akome:'+str(self._device.getSourceID()), no_ack=True)
        self.log("Source queue has been set up: smart_akome:"+str(self._device.getSourceID()))

    def callback(self, ch, method, properties, body):
        self.signalReceived(body.decode())

    def signalReceived(self,signal):
        sig = DeviceSignalFactory.fromJson(signal)
        self.on_signal_received(sig)

#----------------------------------------------------



            

