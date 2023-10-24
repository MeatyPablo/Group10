# ECSE 4230
# Group10
# Blink LED Program
# Zach Blazowski


# imports for code
import RPi.GPIO as GPIO
from time import sleep


# create variables
LEDPin = 17
# turn off GPIO warnings
GPIO.setwarnings(False)

# set GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPin, GPIO.OUT, initial = GPIO.LOW)

# while loop to have LED blink
while True:
    GPIO.output(LEDPin, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(LEDPin, GPIO.LOW)
    sleep(0.5)

GPIO.cleanup()

