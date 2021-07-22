# Chapter 11 - Debugging

# %% Raising exceptions
if True == True:
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
switchLights(mission_16th)
# AssertionError: Neither light is red! {'ns': 'green', 'ew': 'yellow'}
# %% Logging
# factorialLog.py
import logging
logging.basicConfig(level=logging.DEBUG, 
   format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')    
'''
2021-07-21 18:36:14,850 - DEBUG - Some debugging details.
2021-07-21 18:36:14,852 - INFO - The logging module is working.
2021-07-21 18:36:14,852 - WARNING - An error message is about to be logged.
2021-07-21 18:36:14,853 - ERROR - An error has occurred.
2021-07-21 18:36:14,854 - CRITICAL - The program is unable to recover!
'''
# up to you to change the priority you want to see, change level in basicConfig
# ex. logging.ERROR will show only ERROR and CRITICAL messages 
#  and skip the DEBUG, INFO, and WARNING messages
# %% Disabling Logging
import logging
logging.basicConfig(level=logging.INFO, 
    format='%(asctime)s - %(levelname)s -  %(message)s')
logging.critical('Critical error! Critical error! 1')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error! 2')
logging.error('Error! Error!')
# 2021-07-21 18:56:04,816 - CRITICAL -  Critical error! Critical error! 1

# %% Logging to a file
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, 
    format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Testing logging to a file 123...')
# %%
