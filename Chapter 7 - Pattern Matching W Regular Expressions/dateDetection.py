# Practice Project: Date Detection
import pyperclip, re

def validateDate(day: int, month: int, year: int) -> bool:
    '''Returns a bool whether the date is valid.

    Parameters
    ------------
    day: int
        The day value of the date
    month: int
        The month value of the date
    year: int
        The year value of the date

    Returns
    ---------
    bool
        True if date is valid, otherwise False
    '''
    if month in [4,6,9,11]:
        return day <= 30
    elif month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            leapYear = True
            return day <= 29
        else:
            leapYear = False
            return day <= 28
    else:
        return day <= 31

def main():
    dateRegex = re.compile(r'''
        ([0-2]\d|3[0-1])  # DD day
        [-./]             # separator
        (0\d|1[0-2])/     # MM month
        [-./]             # separator
        ([1-2]\d{3})      # YYYY year
    ''', re.VERBOSE)
    print(validateDate(29,2,2005))

if __name__ == '__main__':
    main()