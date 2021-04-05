import random
numOfStreaks = 0
for experimentNum in range(10000):
    # code that creates a list of 100 'heads' or 'tails' values
    flips = []
    for _ in range(100):
        flips.append(random.randint(0,1))
    # code that checks if there is a streak of 6 heads or tails in a row
    streak = 0
    for i in range(1,100):
        if flips[i] == flips[i-1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            streak = 0
            numOfStreaks += 1

print('Chance of streak: {}%'.format(numOfStreaks/100/10000))