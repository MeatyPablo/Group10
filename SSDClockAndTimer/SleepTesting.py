# import sleep and our sleep implementation called "Delay"
import time
import Delay

# create for loop too test 1 - 100 seconds
for x in range(100):
    # testing the sleep functionality
    start = time.time()
    time.sleep(x)
    end = time.time()
    elap = end - start

    # testing our sleep implementatin functionlity
    start2 = time.time()
    Delay.delay(x)
    end2 = time.time()
    elap2 = end2 - start2

    # print out the tested time for each method call
    print("Sleep time: " + str(x))
    print("Delay time: " + str(x))
    # print out the sleep and delay actual time compared to tested time
    print("Actual sleep time: " + str(elap))
    print("Actual delay time: " + str(elap2))
 