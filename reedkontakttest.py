import  RPi.GPIO as gpio
import time

reedPin = 17
gpio.setmode(gpio.BCM)
gpio.setup(reedPin, gpio.IN, pull_up_down=gpio.PUD_UP)

try:
    while True:
        if gpio.input(reedPin) == gpio.LOW:
            print("geschlossen")
        else:
            print("offen")

        time.sleep(0.5)
except KeyboardInterrupt:
    print("beende Programm")
    gpio.cleanup()