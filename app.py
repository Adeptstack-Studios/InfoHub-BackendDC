from flask import Flask, jsonify, request
from gpiozero import Button
from gpiozero import LED
from gpiozero import Buzzer
from json import dumps
import requests
import threading
import time
import os

app = Flask(__name__)   

reedPin = 17
ledPin = 27
soundPin = 22
reed = Button(reedPin, pull_up=True)
led = LED(27)
buzzer = Buzzer(22)

isOpen = False
alarm = False
isAlarm = False
sKey = ""

if not os.path.exists("key.txt"):
    open("key.txt", "w")
with open("key.txt", "r") as file:
    sKey = file.read()

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
    global sKey
    global isAlarm
    if sKey == key:
        isAlarm = True
        time.sleep(1)
        isAlarm = False
        return "success"
    else:
        return "authentication error"

def checkIfOpen():
    global isAlarm
    global isOpen
    global alarm
    if not reed.is_pressed:
        isOpen = True
        if alarm:
            isAlarm = True
        print("offen")
    else:
        isOpen = False
        print("geschlossen")

def doAlarm():
    led.toggle()
    buzzer.toggle()

def Timer():
    global isAlarm
    try:
        while True:
            if isAlarm:
                doAlarm()
            else:
                led.off()
                buzzer.off()
            checkIfOpen()
            time.sleep(0.5)  # Jede Sekunde ausführen
    except KeyboardInterrupt:
        print("beende Programm")

thread = threading.Thread(target=Timer, daemon=True)
thread.start()

if __name__ == '__main__':
    app.run()