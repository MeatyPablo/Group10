# import statements
from datetime import datetime
import RPi.GPIO as GPIO
import time as sleep
import Delay

bList = []


hour = 0
minute = 0

# segment G = Q7       Input Wire = Yellow = 13
# segment A = Q5       Input Wire = Blue = 26
# segment B = Q4       Input Wire = Purple =16
# segment F = Q6       Input Wire = Green= 19
# segment C = Q2       Input Wire = Orange = 11
# segment D = Q1       Input Wire = Red = 9
# segment E = Q0       Input Wire = Brown = 10

# the variable names for the currentState ad the pi clocks for he clock pins
currentState = ' '
pound = False
pinCLK = 20
pinCLK2 = 2
pinCLK3 = 3
pinCLK4 = 21

# these are the GPIO pi numbers in BCM mode for the flip flop inputs for A through G
pinG =13
pinA = 26
pinB = 16
pinF =19
pinC = 11
pinD = 9
pinE = 10

# this is the pin number for the asterik (dot)
pinAs = 4
pinLED = 12

# this clk check is to track the individual state of each clock to increment the clock to next segment
clk1Check = False
clk2Check = False
clk3Check = False
clk4Check = False



'''
state = "off"
'''

# create variables fr the keypad that corresspond to the row and colum connected to the raspberry pi
X1 = 17
X2 = 27
X3 = 22
X4 = 23
Y1 = 24
Y2 = 25
Y3 = 5
Y4 = 6

# create an array of the keypad inputs to store the various values of the inputs in keypad functions
keypadArr = [["1", "2", "3", "A"], 
             ["4", "5", "6", "B"], 
             ["7", "8", "9", "C"], 
             ["*", "0", "#", "D"]]

# for ssd list use % (mod) when setting the index of the ssd
ssdList = [-1 , -1, -1 , -1]
clkList = [20, 2, 3, 21] 

# this will store the current place of teh ssdList so that it can increment in listStore function
ssdListCounter = 0
numCurrentTime = 0

# variables for manual to check current blink clock seve segment
blinkCheck = False

# this wil store the state of each seven segment dislay so that it can be reset after a # and a triple B
manualList = [False, False, False, False]


# store the state of the dot so that it turns off after # ad triple B
dotList = [False]

# setup GPIO to board BCM mode and set off the GPIO warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# setup the keypad GPIOs so that colums is in output but rows will be inputs
GPIO.setup(X1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(X2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(X3, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(X4, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Y1, GPIO.IN)
GPIO.setup(Y2, GPIO.IN)
GPIO.setup(Y3, GPIO.IN)
GPIO.setup(Y4, GPIO.IN)

# setup SSD for each GPIO used from seven segment display and the pin clocks
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
    global bList
    # set the row pressed to high
    GPIO.output(rowNum, GPIO.HIGH)
    
    # check all columns for button press
    if GPIO.input(Y1) == 1:
        print(char[0])
        
        print(bList)
        Delay.delay(0.5)
        bList.append(char[0])
        return char[0]
    if GPIO.input(Y2) == 1:
        print(char[1])
        
        print(bList)

        Delay.delay(0.5)
        bList.append(char[1])
        return char[1]
    if GPIO.input(Y3) == 1:
        print(char[2])
        
        print(bList)
        Delay.delay(0.5)
        bList.append(char[2])
        return char[2]
    if GPIO.input(Y4) == 1:
        print(char[3])
        
        print(bList)

        Delay.delay(0.5)
        bList.append(char[3])
        return char[3]

        
    # set GPIO output to low
    GPIO.output(rowNum, GPIO.LOW)

    #return nthig if no press was detcted

    return '!'

# this function will print the dot depending on the dotList boolean stored
def printAST():
    global dotList

    if dotList[0] == True:
        GPIO.output(pinAs, GPIO.HIGH)
    else:
        GPIO.output(pinAs, GPIO.LOW)

   
    GPIO.output(pinCLK, GPIO.HIGH)
    GPIO.output(pinCLK, GPIO.LOW)

# This functions prints the given d flip flop off when called
def printOff(clk):
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.LOW)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinD, GPIO.LOW)
    GPIO.output(pinG, GPIO.LOW)
    GPIO.output(pinF, GPIO.LOW)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)

# this function prints A in the followinig clk called
def printA(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinD, GPIO.LOW)
    GPIO.output(pinG, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)

# this function prints 1 in the followinig clk called
def print1(clk):
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.LOW)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.LOW)
    GPIO.output(pinG, GPIO.LOW)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()
   

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)

# this function prints 2 in the followinig clk called
def print2(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.LOW)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.LOW)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW) 

# this function prints 3 in the followinig clk called
def print3(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.LOW)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)

# this function prints B in the followinig clk called
def printB(clk):
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)


# this function prints 4 in the followinig clk called
def print4(clk):
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.LOW)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW) 

# this function prints 5 in the followinig clk called
def print5(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  

# this function prints 2 in the followinig clk called
def print6(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  


# this function prints C in the followinig clk called
def printC(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.LOW)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.LOW)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  

# this function prints 7 in the followinig clk called
def print7(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.LOW)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.LOW)
    GPIO.output(pinG, GPIO.LOW)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  

# this function prints 8 in the followinig clk called
def print8(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  

# this function prints 9 in the followinig clk called
def print9(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.LOW)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  

# this function prints D in the followinig clk called
def printD(clk):
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.LOW)
    GPIO.output(pinG, GPIO.HIGH)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)  

# this function prints 0 in the followinig clk called
def print0(clk):
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.HIGH)
    GPIO.output(pinE, GPIO.HIGH)
    GPIO.output(pinF, GPIO.HIGH)
    GPIO.output(pinG, GPIO.LOW)
    #GPIO.output(pinAs, GPIO.LOW)
    #printAST()

    GPIO.output(clk, GPIO.HIGH)
    GPIO.output(clk, GPIO.LOW)

# this funcion will check the current state of the clk1check to ensure that the roper seven segment display is changed
def ssdCheck(clk):

    # call in glbal variables
    global clk1Check
    global clk2Check
    global clk3Check
    global clk4Check

    # check if each individual GPIO is being called and then being set to true
    if clk == 20:
        clk1Check = True
        manualList[0] = True
    if clk == 2:
        clk2Check = True
        manualList[1] = True
    if clk == 3:
        clk3Check = True
        manualList[2] = True
    if clk == 21:
        clk4Check = True
        manualList[3] = True

# the pound function will turn off all segments and then display the last numbers stores
def pound():

    # call in global variables that stored necessary information
    global numCurrentTime
    global ssdListCounter
    global ssdList
    global dotList

    #local variable
    tempCounter = 0

    #turn off segments
    printOff(pinCLK)
    printOff(pinCLK2)
    printOff(pinCLK3)
    printOff(pinCLK4)

    #turn of the dot
    dotList[0] = False
    printAST()

    # while loop until temp == #
    temp = "A"
    while temp != '#':
        temp = readKeypad(X4, keypadArr[3])
        Delay.delay(0.5)

    # check if ampm and print dot
    if(numCurrentTime >= 1200):
        print("currentState")
        dotList[0] = True
        printAST()
        
    else:
        dotList[0] = False
        printAST()

    # print out previous time
    while tempCounter < 4:
        printSSD(ssdList[tempCounter], clkList[tempCounter], True)
        tempCounter = tempCounter + 1

# add delay parameter so that when printing automatically compared to user input, the SD can update faster
def printSSD(temp, clk, poundCheck):
    # call in necessary information to perform the function
    global currentState
    global ssdListCounter
    global ssdList


    #continously check each row for buttn press and then store them into the list Store array and call LED on when invalid input
    '''
    if temp > 2 and clk == 20:
        ledOn(True)
        currentState = temp
        Delay.delay(0.1)
    
   
   
    if temp != '!' and int(temp) > 2 and clk == 20:
        ledOn(True)
        currentState = temp
        Delay.delay(0.1)
    el
    '''
    
    if temp == '#':
        pound()
    elif temp == 'A':
        ledOn(True)
        currentState = temp
        Delay.delay(0.1)
    elif temp == '1':
        listStore(poundCheck, temp)
        print1(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay.delay(0.1)
    elif temp == '2':
        listStore(poundCheck, temp)
        ledOn(False)
        print2(clk)
        ssdCheck(clk)
        currentState = temp
        Delay.delay(0.1)
    elif temp == '3':
        listStore(poundCheck, temp)
        print3(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay.delay(0.1)
    elif temp == '4':
        listStore(poundCheck, temp)
        print4(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay.delay(0.1)
    elif temp == '5':
        listStore(poundCheck, temp)
        print5(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay.delay(0.1)
    elif temp == '6':
        listStore(poundCheck, temp)
        print6(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay.delay(0.1)
    elif temp == 'B':
        ledOn(True)
        currentState = temp
        Delay.delay(0.1)
    elif temp == '7':
        listStore(poundCheck, temp)
        print7(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay.delay(0.1)    
    elif temp == '8':
        listStore(poundCheck, temp)
        print8(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay.delay(0.1)
    elif temp == '9':
        listStore(poundCheck, temp)
        print9(clk)
        ssdCheck(clk)
        ledOn(False)
        currentState = temp
        Delay.delay(0.1)
    elif temp == 'C':
        ledOn(True)
        currentState = temp
        Delay.delay(0.1)
    elif temp == '0':
        listStore(poundCheck, temp)
        print0(clk)
        ssdCheck(clk)
        #print("zero bt press read")
        ledOn(False)
        currentState = temp
        Delay.delay(0.1)
    elif temp == 'D':
        ledOn(True)
        currentState = temp
        Delay.delay(0.1)
    elif temp == '*':
        ledOn(True)
        currentState = temp
        Delay.delay(0.1)
    
# this function will store the elements into the ssdList array to reprint after pound function
def listStore(poundCheck, temp):
    global ssdListCounter
    global ssdList
    
    # thi will check if pound press if false and then display the last stored values on the 7SD
    if poundCheck == False:
        ssdList [ssdListCounter % 4] = temp
        ssdListCounter = ssdListCounter + 1
    #print(ssdList)

       
# this will turn the LED on when there is a invalid input called and vice versa
def ledOn(invalid):
    if invalid:
        GPIO.output(pinLED, GPIO.HIGH)
    else: 
        GPIO.output(pinLED, GPIO.LOW) 
    
# This the function for automatic that will be called and change the Pi military time into digitltime
def automatic():
    
    # call in the num current Time and Dot list
    global numCurrentTime
    global dotList

    # stores the current time
    now  = datetime.now()
    currentTime = now.strftime("%H:%M:%S")

    # calculations
    seconds = int(currentTime[6]) * 10 + int(currentTime[7])
    secondsTilMin = 60 - seconds
    numCurrentTime = int(currentTime[0]) *1000 +int(currentTime[1]) * 100+ int(currentTime[3]) *10 +int(currentTime[4])
    # for testing purposes we will comment this out
    '''
    print("TIME: ")
    print(currentTime)  
    '''
    
    if(numCurrentTime <= 99):
            numCurrentTime += 1200
    # printing the time
    printableTime = numCurrentTime
    
    
    # calculate new time if goes beyond 60
    if((numCurrentTime % 100) / 60 >= 1 ):
        printableTime += 40
    
    # calculate PM
    if(numCurrentTime / 1200 >= 1):
        #printAS(pinCLK, True)
        
        dotList[0] = True
        printAST()
        
    else:
        #printAS(pinCLK, False)
        dotList[0] = False
        printAST()
        
    


    # convert to non millitary time
    if(numCurrentTime / 1300 >= 1):
        printableTime -= 1200

    

    # print out on ssd
    printSSD(str(int(printableTime / 1000)), pinCLK, False)
    printSSD(str(int((printableTime / 100) % 10)), pinCLK2, False)
    printSSD(str(int((printableTime / 10) % 10)), pinCLK3, False)
    printSSD(str(int(printableTime % 10)), pinCLK4, False)
    
    '''
    print("THIS IS THE DOT LIST")
    print(dotList)
    '''

    # for loop to wait until secondsTilMin is finished
    for x in range(secondsTilMin * 2):

        # read keypad for pound or b
        bStatus = readKeypad(X2, keypadArr[1])
        bStatus = readKeypad(X4, keypadArr[3])

        # bCheck here
        if BCheck() == True:
            raise Exception

        # pondCheck here
        if bStatus == '#':
            dotList[0] = False
            printAST()
            pound()

        # delay
        Delay.delay(0.5)

    while BCheck() == False:

        # add 1 to numcurrenttime
        numCurrentTime += 1
        printableTime = numCurrentTime

        # calculate new time if goes beyond 60
        if((numCurrentTime % 100) / 60 >= 1 ):
            printableTime += 40

        # calculate PM
        if(numCurrentTime / 1200 >= 1):
            #printAS(pinCLK, True)
            dotList[0] = True
            printAST()
        else:
            dotList[0] = False
            printAST()

            #printAS(pinCLK, False)

        # convert to non millitary time
        if(numCurrentTime / 1300 >= 1):
            printableTime -= 1200

        # print out on ssd
        printSSD(str(int(printableTime / 1000)), pinCLK, False)
        printSSD(str(int((printableTime / 100) % 10)), pinCLK2, False)
        printSSD(str(int((printableTime / 10) % 10)), pinCLK3, False)
        printSSD(str(int(printableTime % 10)), pinCLK4, False)

        # check differences
        print("The current time is below")
        print(datetime.now().strftime("%H:%M:%S"))
        print("The current time on the clock is below")
        tempClockTime = numCurrentTime * 100
        print(tempClockTime)
        print()
        print()

        # start of for loop to check and wait 60 seconds
        for x in range(120):

            # read keypad for pound or b
            bStatus = readKeypad(X2, keypadArr[1])
            bStatus = readKeypad(X4, keypadArr[3])

            # bCheck here
            if BCheck() == True:
                raise Exception

            # pondCheck here
            if bStatus == '#':
                dotList[0] = False
                printAST()
                printOff(pinCLK)
                pound()

            # delay
            Delay.delay(0.5)
    init()
    begin()

# blink function that will blink the called in clock
def blink(clk):
    global blinkCheck

    if blinkCheck == True:
        printOff(clk)
        blinkCheck = False
    else:
        print8(clk)
        blinkCheck = True

    Delay.delay(0.5)


# manual function
def manual():
    global ssdList
    
    # fix the checks here
    global clk1Check
    global clk2Check
    global clk3Check
    global clk4Check

    # print off
    printOff(pinCLK)
    printOff(pinCLK2)
    printOff(pinCLK3)
    printOff(pinCLK4)

    # sets the manual list items to false
    manualList[0] = False
    manualList[1] = False
    manualList[2] = False
    manualList[3] = False

    print("MANUAL LIST")
    print(manualList)

    print("THIS IS THE STATE OF THE FIRST CLOCK")
    print(clk1Check)

    # check for first ssd
    while manualList[0] == False:
        blink(pinCLK)

        # first row
        temp = readKeypad(X1, keypadArr[0])
        if temp != '!' and int(temp) > 2:
            ledOn(True)
            Delay.delay(0.1)
        else:
            printSSD(temp, pinCLK, False)

        # second row
        temp = readKeypad(X2, keypadArr[1])
        if temp != '!' and int(temp) > 2:
            ledOn(True)
            Delay.delay(0.1)
        else:
            printSSD(temp, pinCLK, False)
        
        # third row
        temp = readKeypad(X3, keypadArr[2])
        if temp != '!' and int(temp) > 2:
            ledOn(True)
            Delay.delay(0.1)
        else:
            printSSD(temp, pinCLK, False)

        # fourth row
        temp = readKeypad(X4, keypadArr[3])
        if temp != '!' and int(temp) > 2:
            ledOn(True)
            Delay.delay(0.1)
        else:
            printSSD(temp, pinCLK, False)
        

    # check second ssd
    while manualList[1] == False:
        blink(pinCLK2)

        # first row
        temp = readKeypad(X1, keypadArr[0])
        printSSD(temp, pinCLK2, False)

        # second row
        temp = readKeypad(X2, keypadArr[1])
        if temp != '!' and int(ssdList[0]) == 2 and int(temp) > 4:
            ledOn(True)
            Delay.delay(0.1)
        else:
            printSSD(temp, pinCLK2, False)

        # third row
        temp = readKeypad(X3, keypadArr[2])
        if temp != '!' and int(ssdList[0]) == 2 and int(temp) > 4:
            ledOn(True)
            Delay.delay(0.1)
        else:
            printSSD(temp, pinCLK2, False)

        # fourth row
        temp = readKeypad(X4, keypadArr[3])
        if temp != '!' and int(ssdList[0]) == 2 and int(temp) > 4:
            ledOn(True)
            Delay.delay(0.1)
        else:
            printSSD(temp, pinCLK2, False)

    # hour calc
    hourTime = int(ssdList[0]) * 10 +int(ssdList[1])
    printHourTime = hourTime
    if(hourTime >= 12 and hourTime <= 23):
        dotList[0] = True
        printAST()
    else:
        dotList[0] = False
        printAST()
    if(printHourTime < 1):
        printHourTime += 12
    if(hourTime / 13 >= 1):
        printHourTime -= 12
    printSSD(str(int(printHourTime / 10)), pinCLK, True)
    printSSD(str(int(printHourTime % 10)), pinCLK2, True)

    # run first ssd and output
    while manualList[2] == False:
        blink(pinCLK3)

        # first row
        temp = readKeypad(X1, keypadArr[0])
        printSSD(temp, pinCLK3, False)

        # second row
        temp = readKeypad(X2, keypadArr[1])
        if temp != '!' and int(temp) > 5:
            ledOn(True)
            Delay.delay(0.1)
        else:
            printSSD(temp, pinCLK3, False)

        # third row
        temp = readKeypad(X3, keypadArr[2])
        if temp != '!' and int(temp) > 5:
            ledOn(True)
            Delay.delay(0.1)
        else:
            printSSD(temp, pinCLK3, False)

        # fourth row
        temp = readKeypad(X4, keypadArr[3])
        if temp != '!' and int(temp) > 5:
            ledOn(True)
            Delay.delay(0.1)
        else:
            printSSD(temp, pinCLK3, False)

    # run first ssd and output
    while manualList[3] == False:
        blink(pinCLK4)
        temp = readKeypad(X1, keypadArr[0])
        printSSD(temp, pinCLK4, False)
        temp = readKeypad(X2, keypadArr[1])
        printSSD(temp, pinCLK4, False)
        temp = readKeypad(X3, keypadArr[2])
        printSSD(temp, pinCLK4, False)
        temp = readKeypad(X4, keypadArr[3])
        printSSD(temp, pinCLK4, False)

    # init manual timer and start
    numCurrentTime = int(ssdList[0]) *1000 +int(ssdList[1]) * 100+ int(ssdList[2]) *10 +int(ssdList[3])
    print("THIS IS THE NUMCURRENTTIME")
    print(numCurrentTime)
    numCurrentTime -= 1

    # bCheck cde start here
    while BCheck() == False:

        # add 1 to numcurrenttime
        numCurrentTime += 1

        # calculate PM
        if(numCurrentTime >= 1200 and numCurrentTime <= 2359):
            dotList[0] = True
            printAST()
        else:
            dotList[0] = False
            printAST()

        printableTime = numCurrentTime

        # calculate new time if goes beyond 60
        if((numCurrentTime % 100) / 60 >= 1 ):
            printableTime += 40

        if(printableTime <= 99):
            printableTime += 1200

        #if(numCurrentTime >= 1300 and dotList[0] == False):
            #printableTime -= 1200


        # calculate new time if goes beyond 60
        #if((numCurrentTime % 100) / 60 >= 1 ):
            #printableTime += 40

        # convert to non millitary time
        if(numCurrentTime / 1300 >= 1):
            printableTime -= 1200

        # print out on ssd
        printSSD(str(int(printableTime / 1000)), pinCLK, False)
        printSSD(str(int((printableTime / 100) % 10)), pinCLK2, False)
        printSSD(str(int((printableTime / 10) % 10)), pinCLK3, False)
        printSSD(str(int(printableTime % 10)), pinCLK4, False)

        # start of for loop to check and wait 60 seconds
        for x in range(120):

            # read keypad for pound or b
            bStatus = readKeypad(X2, keypadArr[1])
            bStatus = readKeypad(X4, keypadArr[3])

            # bCheck here
            if BCheck() == True:
                raise Exception

            # pondCheck here
            if bStatus == '#':
                dotList[0] = False
                printAST()
                printOff(pinCLK)
                pound()

            # delay
            Delay.delay(0.5)
    init()
    begin()


    

    
# this is our menu function that ill check the user input to call automatic or manual
def menuSSD(temp):
    if temp == 'A':
        print("A was pressed")
        automatic()
    elif temp == 'B':
        print("B was pressed")
        manual()
    elif temp == 'C':
        print("c was pressed")
    elif temp == '#':
        print("c was pressed")
        
# this function will check if there has been three b presses ad return a boolean 
def BCheck():

    # call in global variables
    global bList
    back = False
    #check the last three button presses to see if they are all B and then change the boolean value to true
    if len(bList) >= 3:

        if bList[len(bList) - 3] == 'B':
            if bList[len(bList) - 2] == 'B':
                if bList[len(bList) - 1] == 'B':
                    print("Exit to main menu")
                    bList.append('!')
                    back = True
    return back

#this is our begin function that will check the initial button press and is recursively called
def begin():
    
    while 1 > 0:

        # reset clkCheck
        #initCheck()

        # init if coming back from already using clock
        init()

        # read 1st keypad row
        temp = readKeypad(X1, keypadArr[0])
        BCheck()
        try:
            menuSSD(temp)
        except:
            print("in main menu")
    
        # read 2nd keypad row
        temp = readKeypad(X2, keypadArr[1])
        BCheck()
        try:
            menuSSD(temp)  
        except:
            print("in main menu")
  
        # read 3rd keypad row
        temp = readKeypad(X3, keypadArr[2])
        BCheck()
        try:
            menuSSD(temp)
        except:
            print("in main menu")
 
        # read 4th keypad row
        temp = readKeypad(X4, keypadArr[3]) 
        BCheck()
        try:
            menuSSD(temp)
        except:
            print("in main menu")

# this is the initial state that will turn the LEDS to 00.00
def init():
    #global dotList
    print0(pinCLK)
    print0(pinCLK2)
    print0(pinCLK3)
    print0(pinCLK4)
    dotList[0] = False
    printAST()
    

# start of code
# init ssd to be all off
# left to right ssd
init()
begin()
    





