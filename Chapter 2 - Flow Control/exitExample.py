# Write your code here :-)
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        print('Executing sys.exit()')
        sys.exit()
    print('You typed {0}.'.format(response))
