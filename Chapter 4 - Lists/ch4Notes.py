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

# %% placing a trailing comma after the
# value inside the parentheses indicates
# the only one value in the tuple
type(('hello',))
# %%
type(('hello'))
# Advantages of Tuples:
#   1. convey ordered sequence of values
#       that never change
#   2. b/c they are immutable and their
#       contents don't change, Python
#       can implement some optimizations

# %% list() and tuple() casting fn's
tuple(['cat', 'dog', 5])
# %%
list(('cat', 'dog', 5))
# %%
list('hello')

# %% References (integers are immutable)
spam = 42
cheese = spam
spam = 100
spam # 100
cheese # 42

# %% Lists are mutable
spam = [0, 1, 2, 3, 4, 5]
cheese = spam # reference is being copied, not the list
cheese[1] = 'Hello!'
spam   # [0, 'Hello!', 2, 3, 4, 5]
# the cheese variable refers to the same list
cheese # [0, 'Hello!', 2, 3, 4, 5]

# Variables contain references to values!!!

# %% Identity and the id() fn
bacon = 'Hello'
print(id(bacon)) # 1611495592880
bacon += ' world!' # A new string is made from 'Hello' and ' world!'
print(id(bacon)) # 1611495593968

# %% append() and modifying lists (mutable)
eggs = ['cat', 'dog']
print(id(eggs)) # 1611495516352
eggs.append('moose') # append modifies the list "in place"
print(id(eggs)) # 1611495516352
eggs = ['bat', 'rat', 'cow'] # creates a new list -> new id
print(id(eggs)) # 1611494734400

# append(), extend(), remove(), sort(), reverse()
#  and other list methods modify their lists in place
# Python's automatic garbage collector deletes and values
#  not being referred to by any variables to free up memory

# %% Passing References
# go to passingReference.py
# affects both list and dictionaries

# %% copy Module's copy() and deepcopy() fn's
import copy
spam = ['A', 'B', 'C', 'D']
print(id(spam))
# 1611495516352
cheese = copy.copy(spam)
print(id(cheese))
# 1611494459584
cheese[1] = 42
print(spam)
# ['A', 'B', 'C', 'D']
print(cheese)
# ['A', 42, 'C', 'D']

# If the list you need to copy contains lists,
#  then use the copy.deepcopy() fn instead
# deepcopy() fn will copy inner lists as well



# %%
