# Project: Multi-Clipboard Automatic Messages

import sys, pyperclip

def main():
    TEXT = {'agree': '''Yes, I agree. That sounds fine to me.''',
            'busy': '''Sorry, can we do this later this week or next week?''',
            'upsell': '''Would you consider making this a monthly donation?'''}
    if len(sys.argv) < 2:
        print(f'Usage: python {__file__.split("/")[-1]} [keyphrase] ' \
               '- copy phrase text')
        sys.exit()
    
    keyphrase = sys.argv[1] # first command line arg is the keyphrase

    if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print(f'Text for {keyphrase} copied to clipboard.')
    else:
        print(f'There is no text for {keyphrase}')

if __name__ == '__main__':
    main()
