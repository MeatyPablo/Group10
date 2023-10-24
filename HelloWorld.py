# ECSE 4230
# Group10
# Zach Blazowski
import time
import time as sleep
import Group10.SSDClockAndTimer.Delay as Delay

# code to print hello world
print("Hello World")

def delay(seconds):
    onTime = True
    loops = 1
    neededLoops = 17900* seconds
    while(onTime):
        
        if (loops < neededLoops):
            loops +=1
            #print(loops)
        elif (loops >= neededLoops):
            onTime = False
            #print("THIS IS END")


for x in range(100):
    # time stuff
    start = time.time()
    time.sleep(x)
    end = time.time()
    elap = end - start

    # delay stuff
    start2 = time.time()
    Delay.delay(x)
    end2 = time.time()
    elap2 = end2 - start2

    print("Sleep time: " + str(x))
    print("Delay time: " + str(x))
    print("Actual sleep time: " + str(elap))
    print("Actual delay time: " + str(elap2))

'''
Sleep time: 1
Delay time: 1
Actual sleep time: 1.001046895980835
Actual delay time: 1.000014305114746
Sleep time: 2
Delay time: 2
Actual sleep time: 2.0020837783813477
Actual delay time: 2.0000202655792236
Sleep time: 3
Delay time: 3
Actual sleep time: 3.0030457973480225
Actual delay time: 3.000013589859009
Sleep time: 4
Delay time: 4
Actual sleep time: 4.000107526779175
Actual delay time: 4.000015497207642
Sleep time: 5
Delay time: 5
Actual sleep time: 5.0050835609436035
Actual delay time: 5.000020265579224
Sleep time: 6
Delay time: 6
Actual sleep time: 6.0060789585113525
Actual delay time: 6.000019073486328
Sleep time: 7
Delay time: 7
Actual sleep time: 7.007076740264893
Actual delay time: 7.0000200271606445
Sleep time: 8
Delay time: 8
Actual sleep time: 8.00808596611023
Actual delay time: 8.000019788742065
Sleep time: 9
Delay time: 9
Actual sleep time: 9.009056806564331
Actual delay time: 9.000013828277588
Sleep time: 10
Delay time: 10
Actual sleep time: 10.010082960128784
Actual delay time: 10.000018835067749
Sleep time: 11
Delay time: 11
Actual sleep time: 11.006835699081421
Actual delay time: 11.0000159740448
Sleep time: 12
Delay time: 12
Actual sleep time: 12.012118101119995
Actual delay time: 12.00002384185791
Sleep time: 13
Delay time: 13
Actual sleep time: 13.01310658454895
Actual delay time: 13.000023603439331
Sleep time: 14
Delay time: 14
Actual sleep time: 14.014115810394287
Actual delay time: 14.00002670288086
Sleep time: 15
Delay time: 15
Actual sleep time: 15.009751558303833
Actual delay time: 15.000036239624023
Sleep time: 16
Delay time: 16
Actual sleep time: 16.016112565994263
Actual delay time: 16.000022888183594
Sleep time: 17
Delay time: 17
Actual sleep time: 17.001522541046143
Actual delay time: 17.000014543533325
Sleep time: 18
Delay time: 18
Actual sleep time: 18.018079042434692
Actual delay time: 18.00001811981201
Sleep time: 19
Delay time: 19
Actual sleep time: 19.018781185150146
Actual delay time: 19.00002098083496
Sleep time: 20
Delay time: 20
Actual sleep time: 20.02006506919861
Actual delay time: 20.00001573562622
Sleep time: 21
Delay time: 21
Actual sleep time: 21.013142585754395
Actual delay time: 21.000012636184692
Sleep time: 22
Delay time: 22
Actual sleep time: 22.02206778526306
Actual delay time: 22.00001811981201
Sleep time: 23
Delay time: 23
Actual sleep time: 23.023083925247192
Actual delay time: 23.000014781951904
Sleep time: 24
Delay time: 24
Actual sleep time: 24.02407717704773
Actual delay time: 24.000017166137695
Sleep time: 25
Delay time: 25
Actual sleep time: 25.025078773498535
Actual delay time: 25.00002098083496
'''