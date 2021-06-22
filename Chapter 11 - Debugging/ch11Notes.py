# Chapter 11 - Debugging

# %% Raising exceptions
raise Exception('This is the error message')
# boxPrint.py

# Getting the traceback as a string
# errorExample.py

# %% Assertions
# an assertion is a sanity check to make sure your code isn't
#  doing something obviously wrong
# if the sanity check fails, then an AssertionError exception
#  will be raised
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
ages
# [15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.
# %%
