import shelve, pyperclip, sys

# mcb.pyw - saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - loads keyword to clipboard
#        py.exe mcb.pyw list - loads all keywords to clipboard

def main():
    # command line arg check:
    # {keyword} - the text for the keyword is copied to the clipboard
    # save {keyword} - clipboard contents are saved to keyword
    # list - all the keywords are copied to the clipboard

    with shelve.open('mcb') as mcbShelf:
        if len(sys.argv) == 3:
            if sys.argv[1].lower() == 'save':
                mcbShelf[sys.argv[2]] = pyperclip.paste()
            elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
                del mcbShelf[sys.argv[2]]
        elif len(sys.argv) == 2:
            if sys.argv[1].lower() == 'list':
                pyperclip.copy(str(list(mcbShelf.keys())))
            elif sys.argv[1] in mcbShelf:
                pyperclip.copy(mcbShelf[sys.argv[1]])

if __name__ == '__main__':
    main()