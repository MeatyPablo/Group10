# ECSE 4230
# Group10
# SSD test code
# Zach Blazowski

# imports
import RPi.GPIO as GPIO
import time as sleep
import Group10.SSDClockAndTimer.Delay111 as Delay111


# segment G = Q7       Input Wire = Yellow
# segment A = Q5       Input Wire = Blue
# segment B = Q4       Input Wire = Purple
# segment F = Q6       Input Wire = Green
# segment C = Q2       Input Wire = Orange
# segment D = Q1       Input Wire = Red
# segment E = Q0       Input Wire = Brown



# create variables
X1 = 17
X2 = 27
X3 = 22
X4 = 23
Y1 = 24
Y2 = 25
Y3 = 5
Y4 = 6
keypadArr = [["1", "2", "3", "A"], 
             ["4", "5", "6", "B"], 
             ["7", "8", "9", "C"], 
             ["*", "0", "#", "D"]]


# setup GPIO stuff
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(X1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(X2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(X3, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(X4, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Y1, GPIO.IN)
GPIO.setup(Y2, GPIO.IN)
GPIO.setup(Y3, GPIO.IN)
GPIO.setup(Y4, GPIO.IN)

# function to check the row and column and print the value pressed 
def readKeypad(rowNum, char):
    
    # set the row pressed to high
    GPIO.output(rowNum, GPIO.HIGH)
    
    # check all columns for button press
    if GPIO.input(Y1) == 1:
        print(char[0])
        Delay111.delay(0.5)
    if GPIO.input(Y2) == 1:
        print(char[1])
        Delay111.delay(0.5)
    if GPIO.input(Y3) == 1:
        print(char[2])
        Delay111.delay(0.5)
    if GPIO.input(Y4) == 1:
        print(char[3])
        Delay111.delay(0.5)

        
    # set GPIO output to low
    GPIO.output(rowNum, GPIO.LOW)
    

# while true to consistently check the keypad
while True:
    
    # continously check each row for button press
    readKeypad(X1, keypadArr[0])

    readKeypad(X2, keypadArr[1])
    readKeypad(X3, keypadArr[2])
    readKeypad(X4, keypadArr[3])
    
    
    

