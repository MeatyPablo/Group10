# ECSE 4230
# Group10
# Blink LED Program
# Zach Blazowski

# imports for code
import pigpio
from time import sleep

# create variables
LEDPin = 17
count = 0
frequency = 20


# initialize pigpio
pi= pigpio.pi()

# set the mode of the GPIO pin
pi.set_mode(LEDPin, pigpio.OUTPUT)

# set the frequency
pi.set_PWM_frequency(LEDPin, frequency)
pi.set_PWM_dutycycle(LEDPin, 127.5)

sleep(10)
pi.set_PWM_frequency(LEDPin, 0)
pi.set_PWM_dutycycle(LEDPin, 0)
# create infinite loop for duty cycle
#while True:

