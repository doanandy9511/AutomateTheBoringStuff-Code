# Write your code here :-)
import random

secretNum = random.randint(1,20)
print('I am thinking of a number b/w 1 and 20.')

# prompt user to guess up to 6 times
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNum:
        print('Your guess is too low.')
    elif guess > secretNum:
        print('Your guess is too high.')
    else:
        # This condition is the correct guess!
        break
if guess == secretNum:
    print('Good job! You guessed the number in {0} guesses!'.format(guessesTaken))
else:
    print('Nope. The number I was thinking of was {0}.'.format(secretNum))
