# ECSE 4230
# Group10
# Blink LED Program
# Zach Blazowski

# imports for code
import wiringpi
from time import sleep

# create variables
LEDPin = 17
count = 0

# set up wiring pi library
wiringpi.wiringPiSetupGpio()

# send square wave to LED with desired frequency
wiringpi.softToneCreate(LEDPin)
wiringpi.softToneWrite(LEDPin, 20)

# empty loop and set frequency to 0 when done
while count < 100:
    sleep(1)
    count = count + 1
wiringpi.softToneWrite(LEDPin, 0)



