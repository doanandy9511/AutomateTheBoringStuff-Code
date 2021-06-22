from os import error
import traceback

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

def main():
    try:
        spam()
    except:
        with open('errorInfo.txt', 'w') as errorFile:
            errorFile.write(traceback.format_exc())
        print('The traceback info was written to errorInfo.txt.')

if __name__ == '__main__':
    main()