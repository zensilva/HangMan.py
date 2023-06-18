# Game of HangMan
# Created by Zen Silva
# 11/12/21 last modified

# Initialize
import string

myName = input('what is your name? ')
numLives = int(input('choose difficulty level 1 - 10: '))
print('Hello ' + myName  + ' your game is commensing with '  + str(numLives) + ' live(s)')

# Get Word for play
import random
myWordList = ('ALLOW', 'HORRIBLE', 'FANATICAL', 'MAGIC', 'SHAVE', 'HELLISH', 'STOCKING', 'ABRUPT', 'WHISPER', 'ZIPPER')
random_index = random.randrange(len(myWordList))
myWord = myWordList[random_index]

# Play Game
myWordLetters = set(myWord)  # The letter in the selected word are stored here
abc = set(string.ascii_uppercase)
used_abc = set()  # Start with a blank list
print('Number of letters in the word: ', len(myWord))

# Loop until word is guessed or lives expired, whichever first
while len(myWordLetters) > 0 and numLives > 0:
    if len(used_abc) > 0:
        print('letters used: ', ' '.join(used_abc))
    printWordStatus = [letter if letter in used_abc else '-' for letter in myWord]
    print('The current word is: ', ' '.join(printWordStatus))

    myInput = input('Enter a letter: ').upper()
    if myInput in used_abc:
        print('This letter is already used... Try again! ')
    elif myInput in abc - used_abc:
        used_abc.add(myInput)
        if myInput.upper() in myWordLetters:
            myWordLetters.remove(myInput.upper())
        else:
            numLives = numLives - 1
            print('The letter ', myInput, ' is not in the word')
    else:
        print('Invalid input. Try again! ')
if numLives == 0:
    print('You lost mate... You ran out of lives.')
    print('The word is: ', myWord)
else:
    print('You won mate! The word is ', myWord, '.')
# END :)