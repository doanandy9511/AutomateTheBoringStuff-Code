import pyperclip, re

def main():
    # phone regex
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))? # area code
        [ -.]?             # separator
        (\d{3})            # first 3 digits
        [ -.]?             # separator
        (\d{4})            # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))? # optional extension
    )''', re.VERBOSE)
    # first group would be the entire phone match
    # only applicable to be separated into groups if there is a set
    #  of parentheses around the entire regex pattern string AND
    #  there is at least one inner group

    # email regex
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+ # username
        @                 # @ symbol
        [a-zA-Z0-9.-]+    # domain name
        \.[a-zA-Z]{2,4}   # dot-something
    )''', re.VERBOSE)
    # extra parentheses are not necessary
    # findall can return emails as whole strings

    # find matches in clipboard text
    text = pyperclip.paste() # save string from clipboard into text
    
    matches = []
    for _,area,f3,l4,_,_,ext in phoneRegex.findall(text):
        phoneNum = '-'.join([area, f3, l4])
        if ext != '':
            phoneNum += f' x{ext}'
        matches.append(phoneNum)
        '''
        print('num found')
        i = 0
        for g in groups:
            print(f'{i}: {g}')
            i += 1
        '''
    for emails in emailRegex.findall(text):
        matches.append(emails)

    # copies results to the clipboard
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print(pyperclip.paste())
    else:
        print('No phone numbers or email addresses found.')

if __name__ == '__main__':
    main()

'''
Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 880 420 7240 x 696 or +1 415.863.9900 ext 658 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415-863-9950 ext. 420

Reach Us by Email

General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Conference and Events: conferences@nostarch.com
Help with your order: info@nostarch.com
Reach Us on Social Media
Twitter
Facebook
Instagram
Linkedin
Pinterest
'''