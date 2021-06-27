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
ages.reverse()
ages
# [92, 80, 73, 57, 54, 47, 26, 22, 17, 15]
assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.
# AssertionError  
# Traceback (most recent call last)
# %% Using an Assertion in a Traffic Light Simulation
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), f'Neither light is red! {stoplight}'
switchLights(market_2nd)
# AssertionError: Neither light is red! {'ns': 'yellow', 'ew': 'green'}

# %% Logging
# Using the logging module
import logging
logging.basic
# %%
