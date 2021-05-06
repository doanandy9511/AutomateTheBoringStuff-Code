import pyinputplus as pyip

def main():
    while True:
        response = pyip.inputYesNo('Want to know how to keep an idiot busy for hours?\n')
        if response == 'no':
            break
    print('Thank you. Have a nice day.')

if __name__ == '__main__':
    main()

'''
Want to know how to keep an idiot busy for hours?
sure
'sure' is not a valid yes/no response.
Want to know how to keep an idiot busy for hours?
yes
Want to know how to keep an idiot busy for hours?
y
Want to know how to keep an idiot busy for hours?
Yes
Want to know how to keep an idiot busy for hours?
YES
Want to know how to keep an idiot busy for hours?
YES!!!!
'YES!!!!' is not a valid yes/no response.
Want to know how to keep an idiot busy for hours?
TELL ME HOW TO KEEP AN IDIOT BUSY FOR HOURS.
'TELL ME HOW TO KEEP AN IDIOT BUSY FOR HOURS.' is not a valid yes/no response.
Want to know how to keep an idiot busy for hours?
no
Thank you. Have a nice day.
'''