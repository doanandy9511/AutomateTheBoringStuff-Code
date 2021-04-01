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
# Mutable and Immutable Data Types
name = 'Zophie a cat'
newName = name[:7] + 'the' + name[8:]
newName
# %% Overwriting/replacing, not modifying
eggs = [1,2,3]
eggs = [4,5,6]
eggs
# %% Modifying List
eggs = [1,2,3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
eggs

# %% Tuple Data Type
# 2 differences b/w Tuple and List
#   1. Tuples are declared with ( )
eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))
# %% cont.
#   2. Tuples are immutable
eggs = ('hello', 42, 0.5)
eggs[1] = 99

# %%
type(('hello',))
# %%
type(('hello'))
# Advantages of Tuples:
#   1. convey data that will n