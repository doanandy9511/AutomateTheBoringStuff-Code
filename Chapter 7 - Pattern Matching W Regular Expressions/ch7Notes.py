# %% Finding pattersn of text wiithout regular expressions
# isPhoneNumber.py

# Creating Regex Objects
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Matching Regex Objects
# mo is Match object
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(f'Phone number found: {mo.group()}')

# Review of Regular Expression Matching
'''
1. Import the regex module with import re.
2. Create a Regex object with the re.compile() fn. (Remember to use a raw string.)
3. Pass the string you want to search into the Regex object's search() method.
    This returns a Match object
4. Call the Math object's group() method to return a string of the actual matched text.
web-based regular expression tester - https://pythex.org/
'''

# %% More Pattern Matching w Regular Expressions
# Grouping w Parentheses
import re
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
# '415'
mo.group(2)
# '555-4242'
mo.group(0)
# '415-555-4242'
mo.group() # same as group(0)
# '415-555-4242'
# If you'd like to retrieve all the groups at once,
#  use the groups() method
mo.groups()
# ('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(f'areaCode: {areaCode}, mainNumber: {mainNumber}')
# areaCode: 415, mainNumber: 555-4242

# %% Parentheses in regular expressions
import re
phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
# '(415)'
mo.group(2)
# '555-4242'

# The following characters have special meanings:
#  .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )
# \. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)
# so you'll need to escape them with a backslash

# %% Matching Multiple Groups with the Pipe
# the | character is called a pipe
import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()
# 'Batman'
mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()
# 'Tina Fey'
# can use findall() method to find all matching occurrences
#  (discussed later in the findall() Method section)

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
# 'Batmobile'
mo.group(1)
# 'mobile'
# group parameter only applies to matched text inside
#  the parentheses groups
# *By using the pipe char and grouping parentheses,
#  you can specify several alternative patterns you'd
#  like your regex to match

# %% Optional Matching w the Question Mark (matching zero or one)
import re
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
# 'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
# 'Batwoman'

# Phone number w or w/o area code
phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
# '415-555-4242'
mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()
# '555-4242'

# %% Matching Zero or More w the Star
# the * char means "match zero or more" -- the group
#  that precedes the star can occur any number of times
#  in the text
import re
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
mo1.group()
# 'Batman'
mo2 = batRegex.search('The adventures of Batwoman')
mo2.group()
# 'Batwoman'
mo3 = batRegex.search('The adventures of Batwowowowoman')
mo3.group()
# 'Batwowowowoman'

# %% Matching One or More w the Plus
# while * mrans "match zero or more", the + char
#  means "match one or more"
# the group precending a plus must appear at least
#  ONCE, it is not optional
import re
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batwoman')
mo1.group()
# 'Batwoman'
mo2 = batRegex.search('The adventures of Batwowowowoman')
mo2.group()
# 'Batwowowowoman'
mo3 = batRegex.search('The adventures of Batman')
mo3 == None
# True

# %% Matching Specific Repetitions w Braces
# if you have a group that you want to repeat a 
#  specific number of times, follow the group in
#  your regex with a number in braces
# ex. regex (Ha){3} will match 'HaHaHa'
# ex. regex (Ha){3,5} will match 'HaHaHa',
#            'HaHaHaHa', and 'HaHaHaHaHa'
# ex. regex (Ha){3,} will match three or more instances
# ex. regex (Ha){,5} will match zero to five instances
# These two regular expressions match identical patterns:
# (Ha){3}
# (Ha)(Ha)(Ha)
# These two regular expressions match identical patterns:
# (Ha){3,5}
# ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
import re
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
# 'HaHaHa'
mo2 = haRegex.search('Ha')
mo2 == None
# True

# %% Greedy and Non-greedy Matching
import re
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
# 'HaHaHaHaHa'
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
# 'HaHaHa'
# Note: the question mark can have two meanings
# 1. declaring a non-greedy match
# 2. flagging an optional group
# These meanings are entirely unrelated

# %% The findall() Method
# while search() will return a Match object of the
#  FIRST matched text in the searched string,
#  the findall() method will return the strings of
#  EVERY match in the searched string
import re
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()
# '415-555-9999'

# On the other hand, findall() will ot return a Match object
#  but a list of strings -- as long as there are no
#  groups in the regular expression
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# ['415-555-9999', '212-555-0000']

# If there are groups in the regular expression, then
#  findall() will return a list of tuples
# Each tuple represents a found match, and its items are
#  the matched strings for each group in the regex
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# [('415', '555', '9999'), ('212', '555', '0000')]

# To summarize what the findall() method returns, remember the following:
# * When called on a regex with no groups, such as \d{3}-\d{3}-\d{4}, the method
#   findall() returns a list of string matches, such as ['415-555-9999', '212-555-0000'].
# * When called on a regex that has groups, such as (\d{3})-(\d{3})-(\d{4}), the method
#   findall() returns a list of tuples of strings (one string for each group), such as
#   [('415', '555', '9999'), ('212', '555', '0000')]

# %% Character Classes
# \d is sharthand for the regular expression (0|1|2|3|4|5|6|7|8|9)
# Shorthand character class -> Represents
# \d -> Any numeric digit from 0 to 9.
# \D -> Any charactrer that is NOT a numeric digit from 0 to 9.
# \w -> Any letter, numeric digit, or the underscore character.
#       (Think of this as matching "word" characters.)
# \W -> Any character that is NOT a letter, numeric digit, or the
#       underscore character.
# \s -> Any space, tab, or newline character. (whitespace characters)
#       (Think of this as matching "space" characters.)
# \S -> Any  character that is NOT a space, tab, or newline. 

# Character classes are nice for shortening regular expressions. The character
#  class [0-5] will match only the numbers 0 to 5; this is much shorter than
#  typing (0|1|2|3|4|5). Note that while \d matches digits and \w matches digits,
#  letters, and the underscore, there is no shorthand character class that matches
#  only letters. (Though you can use the [a-zA-Z] character class, as explained next)
import re
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

# %% Making you own character classes
# ex. [aeiouAEIOU] will match any vowel, both lower and uppercase
import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

# You can also include ranges of letters or numbers by using a hypen
# ex. character class [a-zA-Z0-9] will match all lowercase, uppercase
#      letters, and numbers
# Note: inside the square brackets, the normal regular expression
#        symbols are not interpreted as such
# ex. char class [0-5.] will match digits 0 to 5 and a period

# By placing a caret character (^) just after the opening bracket,
#  you can make a negative character class. This will match all the
#  characters that are NOT in the character class
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
# ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 
#  'B', 'B', 'Y', ' ', 'F', 'D', '.']

# %% The Caret and Dollar Sign Characters
# You can also use the caret symbol (^) at the start of a regex to indicate that a
#  match must occur at the BEGINNING of the searched text.
# Likewise, you can put a dollar sign ($) at the end of the regex to indicate the
#  string must END with this regex pattern.
# You can use the ^ and $ together to indicate that the entire string must match the
#  regex -- that is, it's not enough for a match to be made on some subset of the string
import re
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')
# <re.Match object; span=(0, 5), match='Hello'>
beginsWithHello.search('He said hello.') == None
# True

endsWithNum = re.compile(r'\d$')
endsWithNum.search('Your number is 42')
# <re.Match object; span=(16, 17), match='2'>
endsWithNum.search('Your number is forty two.') == None
# True
# %% the r'^\d+$' regular expression string matches strings that both begin and end with
#     one or more numeric characters
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
# <re.Match object; span=(0, 10), match='1234567890'>
wholeStringIsNum.search('12345xyz67890') == None
# True
wholeStringIsNum.search('12 34567890') == None
# True
# "Carrots cost dollars"
# caret comesf irst and the dollar sign comes last

# %% The Wildcard Character
# The . (or dot) character in a regular expression is called a wildcard and will match
#  any character except for a newline
import re
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat']
# note: the dot character will match just ONE character, which is why
#        the match for the text flat is only lat
# to match an actual dot, escape the dot with a backslash \.

# %% Matching Everything w Dot-Star
# Sometimes you will want to match everything and anything
# dot char  -> any single char except the newline
# star char -> zero or more of the preceding character
import re
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Andy Last Name: Doan')
mo.group(1)
# 'Andy'
mo.group(2)
# 'Doan'

# The dot-star uses greedy mode: it will always try to match as much text as possible
# To match any and all text in a non-greedy fashion, use the dot, star, and question mark
#  (.*?)
# Like with braces, the questionmark tells Python to match in a non-greedy way
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()
# '<To serve man>'
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()
# '<To serve man> for dinner.>'

# %% Matching Newlines with the Dot Character
# when passing re.DOTALL as the second arg to re.compile(),
#  the dot char will match ALL characters, including the newline char
noNewlineRegex = re.compile(r'.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# 'Serve the public trust.'
newlineRegex = re.compile(r'.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# 'Serve the public trust.\nProtect the innocent.\nUphold the law.'

# %% REVIEW OF REGEX SYMBOLS
'''
basic regular expression syntax:
* the ? matches zero or  one of the preceding group (ln 82)
* the * matches zero or more of the preceding group (ln 101)
* the + matches one  or more of the preceding group (ln 117)
* the {n} matches exactly n  of the preceding group (ln 134)
* the {n,} matches n or more of the preceding group (ln 141)
* the {,m} matches 0 to m    of the preceding group (ln 142)
* the {n,m} matches at least n and at most m of the preceding group (ln 158)
* {n,m}? or *? or +? performs a non-greedy match of the preceding group (ln 164)
*  Note: * = {0,} + = {1,}
* ^spam means the string must begin with spam (ln 251)
* spam$ means the string must end with spam (ln 251)
* the . matches any character, except newline characters (all when re.DOTALL is passed) (ln 282)
* \d. \w, and \s match a digit, word, or space character, respectively (ln 206)
* \D, \W, and \S match anything except a digit, word, or space character, respectively (ln 206)
* [abc] matches any character between the brackets (such as a, b, or c) (ln 219)
* [^abc] matches any character that isn't between the brackets (ln 243)
'''

# %% Case-insensitive Matching
# to make regex case-insensitive, you can pass re.IGNORE or re.I as a second argument to re.compule()
import re
robocop = re.compile(r'robocop', re.IGNORECASE)
robocop.search('RoboCop is part man, part machine, all cop.').group()
# 'RoboCop'
robocop.search('ROBOCOP protects the innnocent.').group()
# 'ROBOCOP'
robocop.search('Al, why does your programming book talk about robocop so much?').group()
# 'robocop'

# %% Substituting Strings w the sub() Method
# Regular expression can not only find text patterns but can also substitute new text in place
#  of those patterns. The sub() method for Regex objects is passed two arguments.
# The first arg is a string to replace any matchs, the second is the string for the regular
#  expression. The sub() methods returns a string with the substitutions applied.
import re
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Ando gave the secret documents to Agent Pollen.')
# 'CENSORED gave the secret documents to CENSORED.'

# Sometimes you may need to use the matched text itself as part of the substitution.
# In the first argument to sub(), you can type \1, \2, \3, and so on, to mean
#  "Enter the text of group 1, 2, 3, and so on, in the substitution."
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Ando told Agent Cat that Agent Elmo knew Agent Bee was a double agent.')
# 'A**** told C**** that E**** knew B**** was a double agent.'

# %% Managing Complex Regexes
# Regular expressions are fine if the text pattern you need to match is simple. But matching complicated
# text patterns might require long, convoluted regular expressions. You can mitigate this by telling the
# re.compile() fn to ignore whitespace and comments inside the regular expression string
# This "verbose mode" can be eneabled by passing the variable re.VERBOSE as the second arg to re.compile()

#BEFORE
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
#AFTER
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # area code ### or (###) (optional ?)
    (\s|-|\.)?           # separator (' ' or '.') (optional ?)
    \d{3}                # first 3 digits
    (\s|-|\.)            # separator (' ' or '.')
    \d{4}                # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # (spaces, if any) extension
    )''', re.VERBOSE)

# %% Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
# The re.compile() fn takes only a single value as its second arg. You can get around this by combining
#  the re.IGNORECASE, re.DOTALL, and re.VERBOSE variables using the pipe character (|) (bitwise OR operator)

import re
# ex. case-insensitive and includes newlines to match the dot char
someRegexValue = re.compile(r'foo.*', re.IGNORECASE | re.DOTALL)
mo = someRegexValue.search('FOO\nBREHHH')
mo.group()
# ''FOO\nBREHHH'

# ex. including all three options in the second arg would look like this
someRegexValue = re.compile(r'foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# %% Project: Phone # and Email Address Extractor
# phoneAndEmail.py

# %% Practice Question
'''
20. How would you write a regex that matches a number with commas for
every three digits? It must match the following:
'42'
'1,234'
'6,368,745'

but not the following:
'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)
'''
import re
digitRegex = re.compile(r'^\d{1,3}(,\d{3})*$')
mo = digitRegex.search('42')
print(mo.group())
mo = digitRegex.search('1,234')
print(mo.group())
mo = digitRegex.search('6,368,745')
print(mo.group())
mo = digitRegex.search('12,34,567')
print(mo == None)
mo = digitRegex.search('1234')
print(mo == None)
# %%
'''
21. How would you write a regex that matches the full name of 
someone whose last name is Watanabe? You can assume that the 
first name that comes before it will always be one word that 
begins with a capital letter. The regex must match the following:
'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'

but not the following:
'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)
'''
import re
# either * or +
WatanbeRegex = re.compile(r'^[A-Z][A-Za-z]* Watanabe$')
mo = WatanbeRegex.search('Haruto Watanabe')
print(mo.group())
mo = WatanbeRegex.search('Alice Watanabe')
print(mo.group())
mo = WatanbeRegex.search('RoboCop Watanabe')
print(mo.group())
mo = WatanbeRegex.search('haruto Watanabe')
print(mo == None)
mo = WatanbeRegex.search('Mr. Watanabe')
print(mo == None)
mo = WatanbeRegex.search('Watanabe')
print(mo == None)
mo = WatanbeRegex.search('Haruto watanabe')
print(mo == None)

# %%
'''
22. How would you write a regex that matches a sentence where 
the first word is either Alice, Bob, or Carol; the second word 
is either eats, pets, or throws; the third word is apples, cats, 
or baseballs; and the sentence ends with a period? This regex 
should be case-insensitive. It must match the following:

'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:

'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'
'''
sentenceRegex = re.compile(r'''
    ^(Alice|Bob|Carol)\s
    (eats|pets|throws)\s
    (apples|cats|baseballs)\.$
    ''', re.VERBOSE | re.IGNORECASE)
mo = sentenceRegex.search('Alice eats apples.')
print(mo.group())
mo = sentenceRegex.search('Bob pets cats.')
print(mo.group())
mo = sentenceRegex.search('Carol throws baseballs.')
print(mo.group())
mo = sentenceRegex.search('Alice throws Apples.')
print(mo.group())
mo = sentenceRegex.search('BOB EATS CATS.')
print(mo.group())
mo = sentenceRegex.search('RoboCop eats apples.')
print(mo == None)
mo = sentenceRegex.search('ALICE THROWS FOOTBALLS.')
print(mo == None)
mo = sentenceRegex.search('Carol eats 7 cats.')
print(mo == None)

# PRACTICE PROJECTS
# Date Detection
# dateDetection.py