# this function is our implementation of sleep
# that will take on a parameter seconds and essentially loop and increment 
#loops until loops is greater than neededloops after onTime is set to false
def delay(seconds):

    # create bolean variable to control while loop
    onTime = True

    # create "loops" with will be iterated by 1 
    loops = 1

    # calculate the needed loops per second
    neededLoops = 17900*260* seconds

    # start of the while loop that will be called off within function
    while(onTime):
        
        # if statement, if loops is less than neededloops, iterate and pass
        if (loops < neededLoops):
            loops +=1
            pass
        # else stop the while loop
        elif (loops >= neededLoops):
            onTime = False
            loops = 1

            #print out when the program ends
            print("THIS IS END")

# Test cases
#delay(5)