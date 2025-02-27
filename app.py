from flask import Flask, jsonify, request
from json import dumps
import board
import requests

app = Flask(__name__)

gpio = 4 # BCM Numbering
isOpen = False
alarm = False

@app.route('/GetCurrentValues')
def send_json():
    
    jsondict = {"IsOpen": isOpen, "IsAlarm": alarm }

    data = dumps(jsondict)
    print("send")
    return data


if __name__ == '__main__':
    app.run()