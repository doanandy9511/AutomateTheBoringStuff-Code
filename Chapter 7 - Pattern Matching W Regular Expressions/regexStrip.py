import re

def regexStrip(inputStr: str, stripChar: str = None):
    '''Takes a string and removes whitespace characters or the specified 
    characters from the beginning and end of the string and returns this 
    new string.

    Parameters
    ----------
    inputStr: str
        The string to be stripped
    stripChar: str, optional
        The specified characters to be removed from the string

    Returns
    -------
    string
        a string that represents the stripped version of the input string
        (default is None)
    '''
    if stripChar:
        _regexStrip = re.compile(rf'^[{stripChar}]*(.*?)[{stripChar}]*$')
    else:
        _regexStrip = re.compile(r'^\s*(.*?)\s*$')
    mo = _regexStrip.search(inputStr)
    if mo == None:
        return ''
    return mo.group(1)

def main():
    print(regexStrip(' Ando Doan          '))
    print(regexStrip(',,,,,rrttgg.....banarna....rrr',',.grt'))

if __name__ == '__main__':
    main()