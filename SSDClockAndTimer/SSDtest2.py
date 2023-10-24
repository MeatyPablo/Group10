# ECSE 4230
# Group10
# SSD test code
# Zach Blazowski

# imports
import RPi.GPIO as GPIO
import time as sleep
import Group10.SSDClockAndTimer.Delay111 as Delay111


# segment G = Q7       Input Wire = Yellow = 13
# segment A = Q5       Input Wire = Blue = 26
# segment B = Q4       Input Wire = Purple =16
# segment F = Q6       Input Wire = Green= 19
# segment C = Q2       Input Wire = Orange = 11
# segment D = Q1       Input Wire = Red = 9
# segment E = Q0       Input Wire = Brown = 10

currentAs = False
currentState = ' '
pound = False
pinCLK = 20
pinCLK2 = 2
pinCLK3 = 3
pinCLK4 = 21
pinG =13
pinA = 26
pinB = 16
pinF =19
pinC = 11
pinD = 9
pinE = 10
pinAs = 4
pinLED = 12
clk1Check = False
clk2Check = False
clk3Check = False
clk4Check = False



state = "off"


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
ssdList = [-1, -1, -1 , -1]
clkList = [20, 2, 3, 21] 
ssdListCounter = 0


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

# setup SSD
GPIO.setup(pinA , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinB , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinC , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinD , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinE , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinF , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinG , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinAs , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinCLK , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinCLK2 , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinCLK3 , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinCLK4 , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pinLED , GPIO.OUT, initial = GPIO.LOW)








# function to check the row and column and print the value pressed 
def readKeypad(rowNum, char):
    
    # set the row pressed to high
    GPIO.output(rowNum, GPIO.HIGH)
    
    # check all columns for button press
    if GPIO.input(Y1) == 1:
        print(char[0])
        Delay111.delay(0.1)
        return char[0]
    if GPIO.input(Y2) == 1:
        print(char[1])
        Delay111.delay(0.1)
        return char[1]
    if GPIO.input(Y3) == 1:
        print(char[2])
        Delay111.delay(0.1)
        return char[2]
    if GPIO.input(Y4) == 1:
        print(char[3])
        Delay111.delay(0.1)
        return char[3]

        
    # set GPIO output to low
    GPIO.output(rowNum, GPIO.LOW)

    #return nthig if no press was detcted

    return '!'

def printAS(pinCLK):

    global currentAs

    GPIO.output(pinAs, GPIO.HIGH)
    GPIO.output(pinCLK, GPIO.HIGH)
    GPIO.output(pinCLK, GPIO.LOW)

    '''
    if currentAs: 
        GPIO.output(pinAs, GPIO.LOW)
        currentAs = False
    else:
        GPIO.output(pinAs, GPIO.HIGH)
        currentAs = True

    GPIO.output(pinCLK, GPIO.HIGH)
    GPIO.output(pinCLK, GPIO.LOW)
    '''
    
def printOff(clk):
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.LOW)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinD, GPIO.LOW)
    GPIO.output(pinG, GPIO.LOW)
    GPIO.output(pinF, GPIO.LOW)
    GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)

def printA(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinD, GPIO.LOW)
    GPIO.output(pinG, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)

def print1(clk):
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.LOW)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.LOW)
    GPIO.output(pinG, GPIO.LOW)
    #GPIO.output(pinAs, GPIO.LOW)
   

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)

def print2(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.LOW)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.LOW)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW) 

def print3(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)  
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.LOW)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)



def printB(clk):
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)



def print4(clk):
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.LOW)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW) 


def print5(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  


def print6(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  



def printC(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.LOW)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.LOW)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  

def print7(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.LOW)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.LOW)
    GPIO.output(pinG, GPIO.LOW)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  


def print8(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  



def print9(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  


def printD(clk):
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.LOW)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  


def print0(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.LOW)
    #GPIO.output(pinAs, GPIO.LOW)

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)

'''
pinCLK = 20
pinCLK2 = 2
pinCLK3 = 3
pinCLK4 = 21
pinG =13

'''

def ssdCheck(clk):
    global clk1Check
    global clk2Check
    global clk3Check
    global clk4Check

    if clk == 20:
        clk1Check = True
    if clk == 2:
        clk2Check = True
    if clk == 3:
        clk3Check = True
    if clk == 21:
        clk4Check = True


def pound():
    global ssdListCounter
    global ssdList

    #local variable
    tempCounter = 0

    #turn off segments
    printOff(pinCLK)
    printOff(pinCLK2)
    printOff(pinCLK3)
    printOff(pinCLK4)
    Delay111.delay(0.5)

    temp = "A"
    while temp != '#':
        temp = readKeypad(X4, keypadArr[3])
        Delay111.delay(0.5)

    # retired cs major
    printAS(pinCLK)

    while tempCounter < ssdListCounter:
        printSSD(ssdList[tempCounter], clkList[tempCounter], True)
        tempCounter = tempCounter + 1








def printSSD(temp, clk, poundCheck):
    global currentState
    global ssdListCounter
    global ssdList


    '''
    if temp == '#':
        printOff(clk)
        Delay.delay(1)
        temp2 = "A"
        while temp2 != '#':
            temp2 = readKeypad(X4, keypadArr[3])
        #Delay.delay(1)
        temp = currentState
    '''
    #continously check each row for butt
    if temp == '#':
        pound()
    elif temp == 'A':
        ledOn(True)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == '1':
        listStore(poundCheck, temp)
        print1(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == '2':
        listStore(poundCheck, temp)
        ledOn(False)
        print2(clk)
        ssdCheck(clk)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == '3':
        listStore(poundCheck, temp)
        print3(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == '4':
        listStore(poundCheck, temp)
        print4(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == '5':
        listStore(poundCheck, temp)
        print5(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == '6':
        listStore(poundCheck, temp)
        print6(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == 'B':
        ledOn(True)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == '7':
        listStore(poundCheck, temp)
        print7(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay111.delay(0.1)    
    elif temp == '8':
        listStore(poundCheck, temp)
        print8(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == '9':
        listStore(poundCheck, temp)
        print9(clk)
        ssdCheck(clk)
        ledOn(False)
        Delay111.delay(0.1)
    elif temp == 'C':
        ledOn(True)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == '0':
        listStore(poundCheck, temp)
        print0(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == 'D':
        ledOn(True)
        currentState = temp
        Delay111.delay(0.1)
    elif temp == '*':
        printAS(clk)
        #ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay111.delay(0.1)
        #printAS(clk)
        
      
    
def listStore(poundCheck, temp):
    global ssdListCounter
    global ssdList
    if poundCheck == False:
        #print(ssdListCounter)
        ssdList [ssdListCounter] = temp
        ssdListCounter = ssdListCounter + 1


def ledOn(invalid):
    if invalid:
        GPIO.output(pinLED, GPIO.HIGH)
    else: 
        GPIO.output(pinLED, GPIO.LOW) 


'''
while True:
   
    temp = readKeypad(X1, keypadArr[0])
    printSSD(temp)
    temp = readKeypad(X2, keypadArr[1])
    printSSD(temp)
    temp = readKeypad(X3, keypadArr[2])
    printSSD(temp)
    temp = readKeypad(X4, keypadArr[3])
    printSSD


'''

# start of code
# init ssd to be all off
printOff(pinCLK)
printOff(pinCLK2)
printOff(pinCLK3)
printOff(pinCLK4)
printOff(pinCLK)
printOff(pinCLK2)
printOff(pinCLK3)
printOff(pinCLK4)

# left to right ssd
# run first ssd and output
while clk1Check == False:
    temp = readKeypad(X1, keypadArr[0])
    printSSD(temp, pinCLK, False)
    temp = readKeypad(X2, keypadArr[1])
    printSSD(temp, pinCLK, False)
    temp = readKeypad(X3, keypadArr[2])
    printSSD(temp, pinCLK, False)
    temp = readKeypad(X4, keypadArr[3])
    printSSD(temp, pinCLK, False)

    # run first ssd and output
while clk2Check == False:
    temp = readKeypad(X1, keypadArr[0])
    printSSD(temp, pinCLK2, False)
    temp = readKeypad(X2, keypadArr[1])
    printSSD(temp, pinCLK2, False)
    temp = readKeypad(X3, keypadArr[2])
    printSSD(temp, pinCLK2,False)
    temp = readKeypad(X4, keypadArr[3])
    printSSD(temp, pinCLK2, False)

# run first ssd and output
while clk3Check == False:
    temp = readKeypad(X1, keypadArr[0])
    printSSD(temp, pinCLK3, False)
    temp = readKeypad(X2, keypadArr[1])
    printSSD(temp, pinCLK3, False)
    temp = readKeypad(X3, keypadArr[2])
    printSSD(temp, pinCLK3, False)
    temp = readKeypad(X4, keypadArr[3])
    printSSD(temp, pinCLK3, False)

# run first ssd and output
while clk4Check == False:
    temp = readKeypad(X1, keypadArr[0])
    printSSD(temp, pinCLK4, False)
    temp = readKeypad(X2, keypadArr[1])
    printSSD(temp, pinCLK4, False)
    temp = readKeypad(X3, keypadArr[2])
    printSSD(temp, pinCLK4, False)
    temp = readKeypad(X4, keypadArr[3])
    printSSD(temp, pinCLK4, False)

while 1 > 0:
    temp = readKeypad(X4, keypadArr[3])
    printSSD(temp, pinCLK4, False)

ssdlistCounter = 0

   
for x in ssdList:
    print(x)


'''
pinCLK = 20
pinCLK2 = 2
pinCLK3 = 3
pinCLK4 = 21
pinG =13

'''

