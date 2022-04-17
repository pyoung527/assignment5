'''
COMP-216 SEC.004 W22 
Assignment5
Group 7
@author = [
    Young Park,
        ]    
'''

import json
import paho.mqtt.client as mqtt
from tkinter import ttk
import tkinter as Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
try:
    from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
except ImportError:
    from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavigationToolbar2TkAgg
import matplotlib
matplotlib.use("TkAgg")

root = Tk.Tk()
root.wm_title("Embedding in TK")


f = Figure(figsize=(3, 2), dpi=100)
a = f.add_subplot(111)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8")
    data_json = json.loads(data)
    x = data_json['array']['x']
    y = data_json['array']['y']
    a.plot(x, y)

    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


topic = 'COMP216Sec004Group7'
broker = 'mqtt.eclipseprojects.io'


client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect(broker, 1883)

client.subscribe(topic)
client.loop_start()
Tk.mainloop()
