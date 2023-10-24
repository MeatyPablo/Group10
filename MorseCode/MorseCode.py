# import statements
#import RPi.GPIO as GPIO
import time
import simpleaudio as sa
import numpy as np
import RPi.GPIO as GPIO

# create frequency tht will be generated in Hz and sampling rate
Frequency = 500
Fs = 44100 
TIMEPERIOD = 0.5

# setup GPIO
pinLED = 2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT, initial = GPIO.LOW)

# duraion of tone that will be created
seconds = 10

#generate an array that will make the sine wave
t = np.linspace(0, seconds, seconds*Fs, False)

# create the sine wave
note = np.sin(Frequency*t*2*np.pi)

# ensures audio input is within range
Audio = 4*note*(2**15 - 1)/np.max(np.abs(note))

# converts audio into 16-bit format
Audio = Audio.astype(np.int16)

# play object created t start audio playback

'''
sa.play_buffer(Audio, 1 , 2, Fs)
time.sleep(10)
sa.stop_all()
'''
# create dot function
def playDot():
    sa.play_buffer(Audio, 1 , 2, Fs)
    GPIO.output(pinLED, GPIO.HIGH)
    time.sleep(TIMEPERIOD)
    sa.stop_all()
    GPIO.output(pinLED, GPIO.LOW)

# create dash function
def playDash():
    sa.play_buffer(Audio, 1 , 2, Fs)
    GPIO.output(pinLED, GPIO.HIGH)
    time.sleep(TIMEPERIOD * 3)
    sa.stop_all()
    GPIO.output(pinLED, GPIO.LOW)

# function to play command
def playCommand(num):

    # case statement
    if num == 0: # sound for attention
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
    elif num == 1: # sound for over
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
    elif num == 2: # sound for out
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()




    
# function to play a single letter
def playLetter(letter):

    # case statment
    if letter == 'A':
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == 'B':
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'C':
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'D':
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'E':
        playDot()
    elif letter == 'F':
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'G':
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'H':
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'I':
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'J':
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == 'K':
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == 'L':
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'M':
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == 'N':
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'O':
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == 'P':
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'Q':
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == 'R':
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'S':
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == 'T':
        playDash()
    elif letter == 'U':
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == 'V':
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == 'W':
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == 'X':
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == 'Y':
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == 'Z':
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == '1':
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == '2':
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == '3':
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == '4':
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDash()
    elif letter == '5':
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == '6':
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == '7':
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == '8':
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == '9':
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDot()
    elif letter == '0':
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()
        time.sleep(TIMEPERIOD)
        playDash()

# function to play a single word
def playWord(word):

    # loop through a word and beep it out
    for char in word:

        # set upper case and play each char
        playLetter(char.upper())
        time.sleep(TIMEPERIOD * 3)

    # wait after playing word
    time.sleep(TIMEPERIOD * 7)

# testing


