#A number guessing game. Computer generates a random number
#which you have to guess.

import random
import os

#Clear the console
clear = lambda: os.system('cls')
clear()

#Declare random number & number of tries
randomNumber = random.randint(1, 20)
tries = 5

#Game loop
def numberGuess(tries) :
    try :
        guessedNumber = int(input())

        while (guessedNumber != randomNumber and tries > 0) :
            if (guessedNumber < randomNumber) :
                tries -= 1
                print('The number you guessed is smaller. ' + 'Tries left: ' + str(tries))
                if(tries > 0) : guessedNumber = int(input())
            elif (guessedNumber > randomNumber) :
                tries -= 1
                print('The number you guessed is larger. ' + 'Tries left: ' + str(tries))
                if(tries > 0) : guessedNumber = int(input())  
        
        if (tries > 0) : print("Congratulations! You guessed right!")
        else : print("You are out of tries. The number I was thinking of was " + str(randomNumber) + ".")
    except : 
        print('Please type in a number value')
        numberGuess(tries)
        
#Run code
print('Hello there, what is your name?')
name = input()
print('Well, ' + str(name) + ", I'm thinking of a number between 1 and 20. Could you guess which number it is?")
numberGuess(tries)
