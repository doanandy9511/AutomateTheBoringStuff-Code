# Project: Adding Bullets to Wiki Markup

import pyperclip

def main():
    text = pyperclip.paste()

    # separate lines and add stars
    lines = text.split('\n')
    # loop through all indices for 'lines' list
    for i in range(len(lines)):
        # add star to each string in 'lines' list
        lines[i] = f'* {lines[i]}'
    text = '\n'.join(lines)
    
    pyperclip.copy(text)

if __name__ == '__main__':
    main()
    