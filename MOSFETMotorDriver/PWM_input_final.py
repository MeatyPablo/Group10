# import statements
import RPi.GPIO as GPIO
import time

# create variables for pin outs using Board
pinRotary = 11
pinDt = 13
pinBT = 15

# variable for counter 
counter = 0
BTState = 1

# create currenttime to for loops per second
currentTime = time.time()

# string state that will be updated to CW/CC/ NONE
state = ""

# create time per second variables
turnsPerSecond = 0
sleepConst = 0.005
noneState = 0


# gpio setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinRotary, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinDt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinBT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# start of code
# init the last clock state
lastClkState = GPIO.input(pinRotary)

# loop and constantly check rotary encoder
while True:

  # set current states
  lastCounter = counter
  lastBTState = BTState

  # check new states read from the rotary encoder
  clkState = GPIO.input(pinRotary)
  dtState = GPIO.input(pinDt)
  BTState = GPIO.input(pinBT)
  
  # check what state it is in
  if clkState != lastClkState:
    
    # if    the clk state and the dt state and will state whether it is CW/CCW/None
    if dtState != clkState:
      counter += 1
      state = "ClockWise"
    else:
      counter -= 1
      state = "CounterClockwise"
  else:
    state = "None"

  # print results
  lastClkState = clkState
  time.sleep(sleepConst)
  if lastCounter != counter and counter % 2 == 1:

    # print ut the stae, the counter though uneeded, and turns per second
    print("State: " + str(state) + " | Counter: " + str(counter - int(counter / 2)) + " | Turns/Second: " + str(round(1 / (time.time() - currentTime - sleepConst), 2)))
    currentTime = time.time()
    noneState = 0
  elif noneState == 0 and int(time.time() - currentTime - sleepConst) >= 1:
    # will display and update terminal when there are no turns within a second
    print("Not Turning")
    noneState = 1
    state = "none"
  
  # print button press
  if lastBTState != BTState and BTState == 0:
    print("Button Pressed")

  

