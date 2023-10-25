import RPi.GPIO as GPIO

pinKey = 4
GPIO.setmode(GPIO.BCM)

GPIO.setup(pinKey, GPIO.IN)

lastPrint = 0

while True:

    stuff = GPIO.input(pinKey)

    if stuff == 0:
        if lastPrint != stuff:
            print(stuff)
        lastPrint = 0
    else:
        if lastPrint != stuff:
            print(stuff)
        lastPrint = 1

    
