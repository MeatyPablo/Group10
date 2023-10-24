import RPi.GPIO as GPIO




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

GPIO.setup(4 , GPIO.OUT, initial = GPIO.LOW)



GPIO.output(4, GPIO.HIGH)