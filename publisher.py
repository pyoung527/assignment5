'''
COMP-216 SEC.004 W22 
Assignment5
Group 7
Members = [
    Young Park,
    Aileen Nicole Alapan,
    Richie Hickey,
    Oscar Quispe Guanoluisa,
    Minusha Shaik
    ]    
'''

import generator
import json
import numpy as np
from json import JSONEncoder
import paho.mqtt.client as mqtt


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)


topic = 'COMP216Sec004Group7'
broker = 'mqtt.eclipseprojects.io'


client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.connect(broker, 1883)
client.loop_start()

for i in range(5):
    numpyData = {"array": generator.generator()}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)
    client.publish(topic, encodedNumpyData)
client.loop_stop()

client.disconnect()
