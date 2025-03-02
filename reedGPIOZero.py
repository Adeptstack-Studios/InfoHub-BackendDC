from gpiozero import Button

# GPIO-Pin für den Reed-Kontakt (z. B. GPIO 17)
reed = Button(17, pull_up=True)  # Interner Pull-up aktiviert

while True:
    if reed.is_pressed:  # Reed-Kontakt geschlossen (LOW)
        print("Reed-Kontakt ist GESCHLOSSEN!")
    else:  # Reed-Kontakt offen (HIGH)
        print("Reed-Kontakt ist OFFEN!")
