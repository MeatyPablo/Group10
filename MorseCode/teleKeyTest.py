

import RPi.GPIO as GPIO

pinKey = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinKey, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:

    stuff = GPIO.input(pinKey)

    if stuff == 0:
        print("Key Touching")
    else:
        print("key not touching")

    
