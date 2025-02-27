from flask import Flask, jsonify, request
from json import dumps
import requests
import threading
import time

app = Flask(__name__)   

gpio = 4 # BCM Numbering
isOpen = False
alarm = False
isAlarm = False
sKey = ""

open("key.txt", "w")
with open("key.txt", "r") as file:
    sKey = file.read()

def Timer():
    while True:
        print("Timer ausgelöst!")
        checkIfOpen()
        time.sleep(1)  # Jede Sekunde ausführen

thread = threading.Thread(target=Timer, daemon=True)
thread.start()

@app.route('/setup/<key>')
def setup(key):
    if sKey == "" and key != "":
        sKey = key
        with open("key.txt", "w") as file:
            file.write(sKey)
        return "success"
    else:
        return "already set up - error"

@app.route('/reset/<key>')
def reset(key):
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
    print('set')
    print(on, key)
    return 'success'

@app.route('/mute/<key>')
def muteAlarm(key):
    print('mute')

@app.route('/test/<key>')
def testAlarm(key):
    print('test')

def checkIfOpen():
    print('open?')

if __name__ == '__main__':
    app.run()