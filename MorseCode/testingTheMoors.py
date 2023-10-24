# import the sound class
import MorseCode

# morse code dictionary
morseDictionary = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}


# function to change words into morse code
def encode(word):
    
    # create array to store morse code
    morseCode = []
    
    # loop through words and convert each letter to morse
    for char in word:
        charUpper = char.upper()
        if charUpper in morseDictionary:
            morseCode.append(morseDictionary[charUpper])
    return ' '.join(morseCode)

# function to print out the morse code in the terminal
def printMessage(encoded, words, output):
    
    # variables and attention print
    wordCounter = 0
    firstRun = True
    
    # main loop for printing the values
    for x in encoded:
        
        if firstRun == True:
            print(x + " | " + words[wordCounter])
            output.write(x + " | " + words[wordCounter] + "\n")
            wordCounter += 1
            firstRun = False
        else:
            print("       " + x + " | " + words[wordCounter])
            output.write("       " + x + " | " + words[wordCounter] + "\n")
            wordCounter += 1




# start of code
# read in the words from a desired file name
try:
    with open("MorseCode/morseInput.txt", 'r') as inputFile:
        # text = inputFile.read()
        text = inputFile.readlines()
except FileNotFoundError:
    print(f"Error: File '{input}' not found.")
    exit(1)


# put in output file and print
output = open("MorseCode/morseOutput.txt", "w")
print("-.-.- | attention")
output.write("-.-.- | attention\n")
for x in text:
    temp = x.split()
    encoded = [encode(word) for word in temp]
    printMessage(encoded, temp, output)
    print("-.- | over")
    output.write("-.- | over\n")
print(".-.-. | out")
output.write(".-.-. | out\n")

# output the morse code in beeps
MorseCode.playCommand(0)
for x in text:
    temp = x.split()
    uhhh = [MorseCode.playWord(word) for word in temp]
    MorseCode.playCommand(1)
MorseCode.playCommand(2)

'''
# split the file into seperate words
words = text.split()

# print out text
print(words)

# change the words to morse code
encoded = [encode(word) for word in words]

# print the words
printMessage(encoded, words)
'''
