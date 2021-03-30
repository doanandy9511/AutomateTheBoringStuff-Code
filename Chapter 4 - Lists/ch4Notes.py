# %%
# test lol
# Enumerate practice
supplies = ['pen','stapler','flamethrower','binders']
for i,item in enumerate(supplies):
    print('Index {0} in supplies is: {1}'.format(i,item))

# random.choice() and random.shuffle() practice
import random
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))
print(random.choice(pets))
print(random.choice(pets))
# You can consider random.choice(someList) to be a shorter 
# form of someList[random.randint(0, len(someList) – 1].

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)
random.shuffle(people)
print(people)

# Sort method for lists (default sort is ASCIIbetical order)
spam = ['a','Z','A','z']
spam.sort(key=str.lower)
print(spam)
spam.sort()
print(spam)

spam = ['cat','dog','moose']
spam.reverse()
print(spam)

# the \ is for line continuation
print('Four score and seven ' + \
    'years ago....')


# %%
