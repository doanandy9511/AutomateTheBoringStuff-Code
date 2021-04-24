# %% Finding pattersn of text wiithout regular expressions
# isPhoneNumber.py

# Creating Regex Objects
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Matching Regex Objects
# mo is Match object
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(f'Phone number found: {mo.group()}')

# Review of REgular Expression Matching
'''
1. Import the regex module with import re.
2. Create a Regex object with the re.compile() fn. (Remember to use a raw string.)
3. Pass the string you want to search into the Regex object's search() method.
    This returns a Match object
4. Call the Math object's group() method to return a string of the actual matched text.
'''