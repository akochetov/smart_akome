import pika
import io
import json
import pickle

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

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='smart_akome', durable = False, exclusive = False, auto_delete = False)

def callback(ch, method, properties, body):
    print(body.decode())
    #loader = io.StringIO(body.decode())
    #signal = json.load(loader)
    
channel.basic_consume(callback,
                      queue='smart_akome',
                      no_ack=True)

print('ping')
channel.start_consuming()
