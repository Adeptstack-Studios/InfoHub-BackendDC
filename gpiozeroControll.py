from gpiozero import LED
from gpiozero import Buzzer
from time import sleep

led = LED(27)
buzzer = Buzzer(22) 

while True:
    led.toggle()
    buzzer.toggle()
    sleep(0.5)
