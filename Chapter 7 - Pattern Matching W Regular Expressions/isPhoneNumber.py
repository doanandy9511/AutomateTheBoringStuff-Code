def isPhoneNumber(text):
    if len(text) != 12:
        return False
    # ###- ###- ## # #
    # 0123 4567 891011
    for i in range(0,3):
        if not text[i].isdecimal:
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal:
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal:
            return False
    return True

def main():
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print(f'Phone number found: {chunk}')
    print('Done')

if __name__ == '__main__':
    main()