import RPi.GPIO as GPIO
import time

# setup GPIO pin
pinMotor = 12 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinMotor, GPIO.OUT)
pwm = GPIO.PWM(pinMotor, 1)

# change frequency
pwm.ChangeFrequency(40)

pwm.start(50)

for x in range(100):
    time.sleep(1)

pwm.stop()