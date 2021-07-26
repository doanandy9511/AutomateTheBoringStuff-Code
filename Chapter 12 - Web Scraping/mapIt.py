# mapIt.py - launches a map in the browser using an 
# address from the command line or clipboard
import webbrowser, sys, pyperclip

def main():
    addr = ''
    if len(sys.argv) > 1:
        # get addr from cmd line
        addr = ' '.join(sys.argv[1:])
    else:
        addr = pyperclip.paste()
    
    webbrowser.open(f'https://www.google.com/maps/place/{addr}')

if __name__ == '__main__':
    main()