# This is a guess the number game.
# modified from: AUTOMATE THE BORING STUFF WITH PYTHON, 2ND EDITION. Copyright © 2020 by Al Sweigart
# ISBN-10: 1-59327-992-2
# ISBN-13: 978-1-59327-992-9
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess x times.
# x random times to guess
timesToGuess =  random.randint(1,10)
print(f'You have {timesToGuess} times to guess the number')
for guessesTaken in range(1, timesToGuess + 1):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!
    print(f'{guessesTaken} try times')

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
