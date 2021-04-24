# %% String Literals, Double Quotes
spam = "That is Alice's cat."
spam

# %% Escape Characters
# an escape character lets you use characters that are 
#  otherwise impossible to put into a string
spam = 'Say hi to Bob\'s mother.'
spam
#           \'            \"   \t       \n         \\
# single quote, double quote, tab, newline, backslash
# %% Raw Strings
# you can place an r before the beginning quotation mark
#  of a string to make it a raw string
print(r'That is Carol\'s cat.')
# raw strings are helpful when typing string values
#  that contain many backslashes, such as file paths
# %% Multiline Strings with Triple Quotes
# catnapping.py
'''Multiline Comments
the # character marks the beginning of a comment for
the rest of the line, but multiline string is often
used for comments that span multiple lines'''

# %% Indexing and Slicing Strings
spam = 'Hello, world!'
spam[0] # 'H'
spam[4] # 'o'
spam[-1] # '!'
spam[0:5] # 'Hello'
spam[:5] # 'Hello'
spam[7:] # 'world!'
# %% in and not in operators w/ strings
# 'Hello' in 'Hello' : True
# '' in 'spam' : True
# 'cats' not in 'cats and dogs' : False

# %% Putting strings inside other strings
name = 'Andy'
age = 420
f'My name is {name}. Next year I will be {age + 1}.'
# 'My name is Andy. Next year I will be 421.'
# %% Useful string methods
# upper(), lower(), isupper(), islower() methods
spam = 'Hello, world!'
spam = spam.upper()
print(spam) # HELLO, WORLD!
spam = spam.lower()
print(spam) # hello, world!

# %%
feeling = input('How are you?\n')
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')
# %%
spam = 'Hello, world!'
spam.islower()
# False
# %%
spam.isupper()
# False
# %%
'HELLO'.isupper()
# True
# %%
'abc12345'.islower()
# True
# %%
'12345'.islower()
# False
# %%
'12345'.isupper()
# False
# %%
'Hello'.upper()
# 'HELLO'
'Hello'.upper().lower()
# 'hello'
'Hello'.upper().lower().upper()
# 'HELLO'
'HELLO'.lower()
# 'hello'
'HELLO'.lower().islower()
# True
# %% the isX() methods
# isalpha() returns True if the string consists only
#  of letters and isn't blank
# isalnum() returns True if the string consists only
#  of letters and numbers and is not blank
# isdecimal() returns True if the string consists only
#  of numeric characters and is not blank
# isspace() returns True if the string consists only
#  of spaces, tabs, and newlines and is not blank
# istitle() returns True if the string consists only
#  of words that begin with an uppercase letter
#  followed by only lowercase letters
'hello'.isalpha()
# True
'hello123'.isalpha()
# False
'hello123'.isalnum()
# True
'hello'.isalnum()
# True
'123'.isdecimal()
# True
'  '.isspace()
# True
'This Is Title Case'.istitle()
# True
'This Is Title Case 123'.istitle()
# True
'This Is not Title Case'.istitle()
# False
'This Is NOT Title Case Either'.istitle()
# False
# %% validateInput.py
# %% startswith() and endswith() methods
'Hello, world!'.startswith('Hello')
# True
'Hello, world!'.endswith('world!')
# True
'abc123'.startswith('abcdef')
# False
'abc123'.endswith('12')
# False
'Hello, world!'.startswith('Hello, world!')
# True
'Hello, world!'.endswith('Hello, world!')
# True

# %% join() and split() methods
', '.join(['cats', 'rats', 'bats'])
# 'cats, rats, bats'
' '.join(['My', 'name', 'is', 'Simon'])
# 'My name is Simon'
'ABC'.join(['My', 'name', 'is', 'Simon'])
# 'MyABCnameABCisABCSimon'
'My name is Simon'.split()
# ['My', 'name', 'is', 'Simon']
'MyABCnameABCisABCSimon'.split('ABC')
# ['My', 'name', 'is', 'Simon']
'My name is Simon'.split('m')
# ['My na', 'e is Si', 'on']
# %% A common use of split() is to splut a multiline
#  string along the newline characters
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''
spam.split('\n')
# ['Dear Alice,',
# 'How have you been? I am fine.',
# 'There is a container in the fridge',
# 'that is labeled "Milk Experiment."',
# '',
# 'Please do not drink it.',
# 'Sincerely,',
# 'Bob']

# %% Splitting Strings with partition() method
# returns a tuple of three substrings
# "before", "separator", "after" substrings
'Hello, world!'.partition('w')
# ('Hello, ', 'w', 'orld!')
# %%
'Hello, world!'.partition('world')
# ('Hello, ', 'world', '!')
# %% if the separator occurs multiple times,
# the method splits the string only on the first occurrence
'Hello, world!'.partition('o')
# ('Hell', 'o', ', world!')
# %% if the separator can't be found, the first string returned
# will be the entire string, and the other two will be empty
'Hello, world!'.partition('XYZ')
# ('Hello, world!', '', '')
# %% you can use the multiple assignment trick to assign
# the three returned strings to three variables
before, sep, after = 'Hello, world!'.partition(' ')
print(before) # 'Hello,'
print(after)  # 'world!'

# %% Justifying  text with the rjust(), ljust(), and center() methods
'Hello'.rjust(10)
# '     Hello'
'Hello'.rjust(20)
# '               Hello'
'Hello, World!'.rjust(20)
# '       Hello, World!'
'Hello'.ljust(10)
# 'Hello     '
# %% an optional argument to rjust() and ljust() will specify
# a fill character other than a space character
'Hello'.rjust(20, '*')
# '***************Hello'
'Hello'.ljust(20, '-')
# 'Hello---------------'
'Hello'.center(20)
# '       Hello        '
'Hello'.center(20, '=')
# '=======Hello========'
# %% picnicTable.py

# %% Removing whitespace with strip(), rstrip(), and lstrip() methods
spam = '    Hello, World   '
spam.strip()
# 'Hello, World'
spam.lstrip()
# 'Hello, World   '
spam.rstrip()
# '    Hello, World'
# %%
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
# passing strip() the argument 'ampS' will tell it to strip occurrences
#  of a, m, p, and capital S from the ends of the string stored in spam
# Note: the order of the characters in the string passed does not matter
#  strip('ampS') = strip('mapS') = strip('Spam')
# %% Numeric values of characters with the ord() and chr() fns
ord('A')
# 65
ord('4')
# 52
ord('!')
# 33
chr(65)
# 'A'
# %% these fns are useful when you need to do an
# ordering or mathematical operation on characters
ord('B')
# 66
ord('A') < ord('B')
# True
chr(ord('A'))
# 'A'
chr(ord('A') + 1)
# 'B'

# %% Copying and pasting strings w/ the pyperclip module
import pyperclip
pyperclip.copy('Hello, world!!')
pyperclip.paste()
# 'Hello, world!!'
# %% Project: Multi-Clipboard Automatic Messages
# ProjectMclip.py

# %% Project: Adding Bullets to Wiki Markup
# ProjectBulletPointAdder.py

# %% Short program: Pig Latin
# pigLat.py

# Practice Projects
# Table Printer: tablePrinter.py