# renameDates.py - Renames filesnames with American MM-DD-YYYY date
#  format to European DD-MM-YYYY

import shutil, os, re

def main():
    datePattern =  re.compile(
        r'''^(.*?)      # all text before the date
        ((0|1)?\d)-     # one or two digits for the month
        ((0|1|2|3)?\d)- # one or two digits for the day
        ((19|20)\d{2})   # four digits for the year
        (.*?)$          # all text after the date
        ''', re.VERBOSE)
    # To keep the group numbers straight, try reading the regex 
    #  from the beginning, and count up each time you encounter 
    #  an opening parenthesis
    '''
    datePattern = re.compile(
        r"""^(1)  # all text before the date
        (2 (3) )- # one or two digits for the month
        (4 (5) )- # one or two digits for the day
        (6 (7) )  # four digits for the year
        (8)$      # all text after the date
        """, re.VERBOSE)
    '''
    
    print(os.path.abspath('.'))

    for amerFilename in os.listdir('.'):
        mo = datePattern.search(amerFilename)
        # skip files without a date
        if mo == None:
            continue
        # get the differnt parts of the filename
        beforePart = mo.group(1)
        monthPart  = mo.group(2)
        dayPart    = mo.group(4)
        yearPart   = mo.group(6)
        afterPart  = mo.group(8)
        # form the European-style filename
        euroFilename = f'{beforePart}{dayPart}-{monthPart}-{yearPart}{afterPart}'
        # get the full, absolute file paths
        absWorkingDir = os.path.abspath('.')
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)
        # rename the files
        print(f'Remaming "{amerFilename}" to "{euroFilename}"...')
        shutil.move(amerFilename, euroFilename) # uncomment after testing

if __name__ == '__main__':
    main()