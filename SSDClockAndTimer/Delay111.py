
# import time library
import time

def delay(seconds):

    # set variabeles to set the time
    currentTime = time.time()

    #seconds = 0
    realInitial = currentTime
    timeElapsed = 0
    # set boolean while loop
    onTime = True

    while (onTime):
        currentTime = time.time()
        timeElapsed = currentTime - realInitial
        if (timeElapsed) < seconds:
            currentTime == time.time()
        elif (timeElapsed >= seconds):
            onTime = False    
           # print(timeElapsed)

#delay(5)
    