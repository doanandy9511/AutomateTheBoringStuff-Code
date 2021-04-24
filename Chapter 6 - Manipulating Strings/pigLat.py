# English to Pig Latin

def main():
    message = input('Enter the English message to translate into Pig Latin:\n')
    VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
    # list of the words in Pig Latin
    pigLatin = []
    for word in message.split():
        # separate the non-letters at the start of this word
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin.append(prefixNonLetters)
            continue

        # separate the non-letters at the end of this word
        suffixNonLetters = ''
        while not word[-1].isalpha():
            suffixNonLetters += word[-1]
            word = word[:-1]
        
        # check if word was in uppercase or title case
        wasUpper = word.isupper()
        wasTitle = word.istitle()

        # make the word lowercase for translation
        word = word.lower()

        # separate the consonants at the start of this word
        prefixConsonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefixConsonants += word[0]
            word = word[1:]

        # add the Pig Latin ending to the word:
        if prefixConsonants == '':
            word += 'yay'
        else:
            word += prefixConsonants + 'ay'

        # set the word back to uppercase or title case
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()
        
        # add the non-letters back to the start or end of the word
        pigLatin.append(f'{prefixNonLetters}{word}{suffixNonLetters}')

    # join all the words back together into a single string
    print(' '.join(pigLatin))

if __name__ == '__main__':
    main()

'''My name is AL SWEIGART and I am 4,000 years old.
Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.'''