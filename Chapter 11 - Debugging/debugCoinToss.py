
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
# fix 1:
toss = random.choice(['heads', 'tails']) # 0 is tails, 1 is heads
# fix 2:
# toss = 'heads' if toss==0 else ('tails' if toss==1 else 'xd')
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')