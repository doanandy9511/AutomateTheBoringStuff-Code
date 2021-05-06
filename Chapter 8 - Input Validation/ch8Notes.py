# %% Typically, input validation is done like this
while True:
    age = input('Enter your age: ')
    try:
        age = int(age)
    except Exception:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break
print(f'Your age is {age}.')

# %% 
# inputStr() - like built-in input() fn but has the general PyInputPlus
#              features. You can also pass a custom validation fn to it
# inputNum() - ensures the user enters a number and returns an int or
#              float, depending on if the num has a decimal point
# inputChoice() - ensures the user enters one of the provided choices
# inputMenu() - is similar to inputChoice(), but provides a menu with
#               numbered or lettered options
# inputDatetime() - ensures the user enters a date and time
# inputYesNo() - ensures the user enters 'yes' or 'no'
# inputBool() - is similar to inputYesNo(), but takes a 'True' or
#               'False' response and returns a Boolean value
# inputEmail() - ensures the user enters a valid email address
# inputFilepath() - ensures the user enters a valid file path and
#                   filename, and can optionally check that a file
#                   with that name exists
# inputPassword() - is like the built-in input(), but displays * characters
#                   as the user types so that passwords, or other
#                   sensitive information, aren't displayed on screen
import pyinputplus as pyip
response = pyip.inputNum()
print(f'Your response was {response}')
# %%
import pyinputplus as pyip
response = pyip.inputInt(prompt='Enter a number: ')
print(f'Your response was {response}')
# %%
import pyinputplus as pyip
response = pyip.inputNum('Enter num: ', min=4)
response = pyip.inputNum('Enter num: ', greaterThan=4)
response = pyip.inputNum('>', min=4, lessThan=6)

# %% The blank Keyword Argument
import pyinputplus as pyip
response = pyip.inputNum('Enter num: ')
response = pyip.inputNum(blank=True)
# use blank = True if you'd like to make input optional so that the user
#  doesn't need to enter anything

# %% The limit, timeout, and default Keyword Arguments
# limit - determines how many attempts a pyip fn will make to receive
#         a valid input before giving up
# timeout - determines how many seconds the user has to enter valid
#           input before the pyip fn gives up
import pyinputplus as pyip
response = pyip.inputNum(limit=2)
# pyinputplus.RetryLimitException will be raised if x attempts are invalid
response = pyip.inputNum(timeout=10)
# pyinputplus.TimeoutException will be raised if a valid input is entered
#  after x seconds

# %% When you use these keyword arguments and also pass a default keyword
#    argument, the fn returns the default value instead of raising
#    an exception
response = pyip.inputNum(limit=2, default='N/A')
print(f'Response is {response}')
# 'N/A' if 2 invalid inputs passed
response = pyip.inputNum(timeout=5, default='N/A')
print(f'Response is {response}')
# 'N/A' after 5 seconds and valid input

# %% The allowRegexes and blockRegexes Keyword Arguments
# you can also use regular expressions to specify whether an input is 
# allowed or not. The allowRegexes and blockRegexes keyword arguments take
# a list of regular expression strings to determine what the pyip fn will
# accept or reject as valid input
# ex. Roman numerals in addition to usual numbers
import pyinputplus as pyip
response = pyip.inputNum(allowRegexes=[r'^[IVXLCDM]+$', r'zero'])
response = pyip.inputNum(allowRegexes=[r'^[ivxlcdm]+$', r'zero'])

# %% ex. won't accept even numbers
response = pyip.inputNum(blockRegexes=[r'[02468]$'])

# %% if you specify both an allowRegexes and blockRegexes argument,
#    the allow list overrides the block list
# ex. allows 'caterpillar' and 'category' but blocks anything else that 
#     the word 'cat' in it
response = pyip.inputStr(allowRegexes=[r'caterpillar', r'category'],
                         blockRegexes=[r'cat'])
'''
cat
This response is invalid.
catastrophe
This response is invalid.
category
>>> response
'category'
'''

# %% Passing a Custom Validation fn to inputCustom()
import pyinputplus as pyip
def addsUpToTen(nums):
    numsList = list(nums)
    for i, digit in enumerate(numsList):
        numsList[i] = int(digit)
    if sum(numsList) != 10:
        raise Exception(f'The digits must add up to 10, not {sum(numsList)}')
    return int(nums) # returns an int form of numbers
response = pyip.inputCustom(addsUpToTen) # no parentheses after addsUpToTen
'''
123
The digits must add up to 10, not 6
1235
The digits must add up to 10, not 11
1234
>>> response
1234
>>> response = pyip.inputCustom(addsUpToTen)                                   
hello
invalid literal for int() with base 10: 'h'
55
>>> response
55
'''
# The inputCustom() fn also supports the general pyip features, such as
#  blank, limit, timeout, default, allowRegexes, and blockRegexes
#  keyword arguments
# Writing your own custom validation function is useful when it's otherwise
#  difficult or impossible to write a regex for valid input, like the
#  example above, 'adds up to 10' validation

# %% Project: How to Keep an Idiot Busy for Hours
# idiot.py

# %% Project: Multiplication Quiz
# multiplicationQuiz.py

# %% Practice Project: Sandwich Maker
# sandwichMaker.py