# Note: If you ever want to modify the value stored in a 
# global variable from in a function, you must use a global 
# statement on that variable.

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)