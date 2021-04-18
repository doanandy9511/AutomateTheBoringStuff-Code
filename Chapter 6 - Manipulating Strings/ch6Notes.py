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
