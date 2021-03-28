import time, sys
indent = 0 # amt of spaces to indent
indentDir = True # whether the indentation is increasing or not

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 0.1 seconds

        if indentDir:
            #  Increase the num of spaces:
            indent += 1
            if indent == 20:
                # Change dir
                indentDir = False
        
        else:
            # Decrease the num of spaces:
            indent -= 1
            if indent == 0:
                # Change dir
                indentDir = True

except KeyboardInterrupt:
    sys.exit()