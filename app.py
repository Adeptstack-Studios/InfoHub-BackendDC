from flask import Flask, jsonify, request
from json import dumps
import requests
import threading
import time
import os

app = Flask(__name__)   

gpio = 4 # BCM Numbering
isOpen = False
alarm = False
isAlarm = False
sKey = ""

if not os.path.exists("key.txt"):
    open("key.txt", "w")
with open("key.txt", "r") as file:
    sKey = file.read()

def Timer():
    while True:
        checkIfOpen()
        time.sleep(1)  # Jede Sekunde ausführen

thread = threading.Thread(target=Timer, daemon=True)
thread.start()

@app.route('/setup/<key>')
def setup(key):
    global sKey
    if sKey == "" and key != "":
        sKey = key
        with open("key.txt", "w") as file:
            file.write(sKey)
        return "success"
    else:
        return "already set up - error"

@app.route('/reset/<key>')
def reset(key):
    global sKey
    if sKey == key and key != "":
        sKey = ""
        with open("key.txt", "w") as file:
            file.write(sKey)
        return "success"
    else:
        return "authentication error"

@app.route('/get')
def send_json():
    jsondict = {"IsOpen": isOpen, "IsAlarm": isAlarm, "Alarm": alarm }
    data = dumps(jsondict)
    print("send")
    return data

@app.route('/set/<int:on>/<key>')
def setAlarm(on, key):
    global sKey
    global alarm
    if sKey == key:
        if on == 0:
            alarm = False
        elif on == 1:
            alarm = True
        else:
            return "ArgumentOutOfRangeException"
    else:
        return "authentication error"
    return "success"

@app.route('/mute/<key>')
def muteAlarm(key):
    global sKey
    global isAlarm
    if sKey == key:
        isAlarm = False
        return "success"
    else:
        return "authentication error"

@app.route('/test/<key>')
def testAlarm(key):
    print('test')

def checkIfOpen():
    print('open?')
    print(alarm)

if __name__ == '__main__':
    app.run()