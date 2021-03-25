# Write your code here :-)
import random, sys

print('ROCK, PAPER, SCISSORS')

# variables to keep track of num  of wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True:
    print('%i Wins, %i Losses, %i Ties'%(wins,losses,ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the game
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # break out of player input loop
        print('Please type one of r, p, s, or q.')

    # display what the player chose:
    if playerMove == 'r':
        print('ROCK vs..')
    elif playerMove == 'p':
        print('PAPER vs..')
    elif playerMove == 's':
        print('SCISSORS vs..')

    # display what the computer chose:
    randNum = random.randint(1,3)
    if randNum == 1:
        computerMove = 'r'
        print('ROCK')
    elif randNum == 2:
        computerMove = 'p'
        print('PAPER')
    elif randNum == 3:
        computerMove = 's'
        print('SCISSORS')

    # display and record the win/loss/tie
    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif playerMove == 'r':
        if computerMove == 's':
            print('You win!')
            wins += 1
        elif computerMove == 'p':
            print('You lose!')
            losses += 1
    elif playerMove == 'p':
        if computerMove == 'r':
            print('You win!')
            wins += 1
        elif computerMove == 's':
            print('You lose!')
            losses += 1
    elif playerMove == 's':
        if computerMove == 'p':
            print('You win!')
            wins += 1
        elif computerMove == 'r':
            print('You lose!')
            losses += 1





