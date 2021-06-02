import traceback
# %% Files and File Paths
# ex. filename project.docx
# ex. path C:\Users\Ando\Documents
from pathlib import Path
Path('spam','bacon','eggs')
# WindowsPath('spam/bacon/eggs')
str(Path('spam','bacon','eggs'))
# 'spam\\bacon\\eggs'

# %%
from pathlib import Path
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for fileName in myFiles:
    print(Path(r'C:\Users\doanando', fileName))
# C:\Users\doanando\accounts.txt
# C:\Users\doanando\details.csv
# C:\Users\doanando\invite.docx

# %% Using the / Operator to Join Paths
# The / operator can be used to combine Path objects and strings. This is
# helpful for modifying a Path object after you've already created it w/
# the Path() function
from pathlib import Path
Path('spam') / 'bacon' / 'eggs'
# WindowsPath('spam/bacon/eggs')
Path('spam') / Path('bacon/eggs1')
# WindowsPath('spam/bacon/eggs1')
Path('spam') / Path('bacon', 'eggs2')
# WindowsPath('spam/bacon/eggs2')

# The pathlib module solves the issue of conflicting path separators
# (\\ in Windows, / in MacOS and Linux) by reusing the / math division
# operator to join paths correctly, no matter what operating system your
# code is running on
# %% ex. of this
from pathlib import Path
homeFolder = Path('C:/Users/doanando')
subFolder = Path('spam')
homeFolder / subFolder
# WindowsPath('C:/Users/doanando/spam')
print(homeFolder / subFolder)
# 'C:\\Users\\doanando\\spam'

# only thing to keep in mind when using the / operator for joining paths
# is that one of the first two values must be a Path object
try:
    'spam' / 'bacon' / 'eggs'
except Exception as e:
    traceback.print_exc()
    print()
# error
# %% The Current Working Directory
from pathlib import Path
import os
Path.cwd()
# WindowsPath('c:/Users/doanando/Documents/GitHub/AutomateTheBoringStuff-Code/Chapter 9 - Reading and Writing Files')
os.chdir('C:/Windows/System32')
print(Path.cwd())
# WindowsPath('C:/Windows/System32')
os.getcwd() # old way for getting cwd as str
# 'C:\\Windows\\System32'
try:
    os.chdir('C:/ThisFolderDoesNotExist')
except Exception as e:
    traceback.print_exc()
    print()
# %% The Home Directory
from pathlib import Path
Path.home()
# WindowsPath('C:/Users/doanando')

# %% Absolute vs. Relative Paths
# abs path - always begins with the root folder
# rel path - relative to the program's current working directory
# dot (.) - "this directory"
# dot-dot (..) - "the parent folder"

# the .\ at the start of a relative path is optional
# ex. .\spam.txt and spam.txt refer to the same file

# Creating New Folders Using the os.makedirs() fn
import os
os.makedirs('C:\\delicious\\walnut\\waffles')
# %% create a spam folder under the home folder on my computer
from pathlib import Path
Path(r'C:\Users\doanando\spam').mkdir()
# mkdir() can only make one directory at a time
# it won't make several subdirectories at once like os.makedirs()

# %% Handling Absolute and Relative Paths
from pathlib import Path
Path.cwd()
# WindowsPath('c:/Users/Ando/Documents/GitHub/AutomateTheBoringStuff-Code/Chapter 9 - Reading and Writing Files')
Path.cwd().is_absolute()
# True
Path('spam/bacon/eggs').is_absolute()
# False

# %%
Path('my/relative/path')
# WindowsPath('my/relative/path')
Path.cwd() / Path('my/relative/path')
# WindowsPath('c:/Users/Ando/Documents/GitHub/AutomateTheBoringStuff-Code/Chapter 9 - Reading and Writing Files/my/relative/path')
Path.home() / Path('my/relative/path')
# WindowsPath('C:/Users/Ando/my/relative/path')

# %%
os.path.abspath('.')
# 'c:\\Users\\Ando\\Documents\\GitHub\\AutomateTheBoringStuff-Code\\Chapter 9 - Reading and Writing Files'
os.path.abspath('.\\Scripts')
# 'c:\\Users\\Ando\\Documents\\GitHub\\AutomateTheBoringStuff-Code\\Chapter 9 - Reading and Writing Files\\Scripts'
os.path.isabs('.')
# False
os.path.isabs(os.path.abspath('.'))
# True

# %%
os.path.relpath('C:\\Windows', 'C:\\')
# 'Windows'
os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
# '..\\..\\Windows'

# %% Getting the Parts of a File Path
p = Path('C:/Users/Ando/spam.txt')
p.anchor
# 'C:\\'
p.parent
# WindowsPath('C:/Users/Ando')
p.name
# 'spam.txt'
p.stem
# 'spam'
p.suffix
# '.txt'
p.drive # only Windows Path objects have this
# 'C:'

# %%
from pathlib import Path
Path.cwd()
# WindowsPath('c:/Users/Ando/Documents/GitHub/AutomateTheBoringStuff-Code/Chapter 9 - Reading and Writing Files')
Path.cwd().parents[0]
# WindowsPath('c:/Users/Ando/Documents/GitHub/AutomateTheBoringStuff-Code')
Path.cwd().parents[1]
# WindowsPath('c:/Users/Ando/Documents/GitHub')
Path.cwd().parents[2]
# WindowsPath('c:/Users/Ando/Documents')
Path.cwd().parents[3]
# WindowsPath('c:/Users/Ando')
Path.cwd().parents[4]
# WindowsPath('c:/Users')
Path.cwd().parents[5]
# WindowsPath('c:/')

# %%
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(calcFilePath)
# 'calc.exe'
os.path.dirname(calcFilePath)
# 'C:\\Windows\\System32'
os.path.split(calcFilePath)
# ('C:\\Windows\\System32', 'calc.exe')
(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
# ('C:\\Windows\\System32', 'calc.exe')
calcFilePath.split(os.sep)
# ['C:', 'Windows', 'System32', 'calc.exe']

# %% Finding File Sizes and Folder Contents
os.path.getsize('C:\\Windows\\System32\\calc.exe')
# 27648
os.listdir('C:\\Windows\\System32')
# many files lmao
totalSize = 0
for file in os.listdir('C:\\Windows\\System32'):
    totalSize += os.path.getsize(os.path.join('C:\\Windows\\System32', file))
print(totalSize)
# 2367391244

# %% Modifying a List of Files Using Glob Patterns
from pathlib import Path
p = Path('C:/Users/doanando/Desktop')
p.glob('*')
# <generator object Path.glob at 0x000001F559529350>
list(p.glob('*'))
'''
[WindowsPath('C:/Users/doanando/Desktop/Among Us.url'),
 WindowsPath('C:/Users/doanando/Desktop/Ando Documents'),
 --snip--
 WindowsPath('C:/Users/doanando/Desktop/Zoom.lnk'),
 WindowsPath('C:/Users/doanando/Desktop/µTorrent.lnk')]
'''
# The asterisk (*) stands for "multiple of any characters"
list(p.glob('*.txt')) # List all text files
# [WindowsPath('C:/Users/doanando/Desktop/atbsch9.txt')]
list(p.glob('project?.docx'))
'''
[WindowsPath('C:/Users/doanando/Desktop/project1.docx'),
 WindowsPath('C:/Users/doanando/Desktop/project2.docx')]
'''
list(p.glob('*.?x?'))
'''
[WindowsPath('C:/Users/doanando/Desktop/atbsch9.txt'),
 WindowsPath('C:/Users/doanando/Desktop/OOSU10.exe')]
'''
# %% If you want to perform some operation on every file
# in a directory, you can use either os.listdir(p) or p.glob('*')
p = Path('C:/Users/doanando/Desktop')
for textFilePathObj in p.glob('*.txt'):
    print(textFilePathObj) # Prints the Path object as a string
    # Do somesing w/ the text file
'''
C:\Users\doanando\Desktop\atbsch9 - Copy (2).txt
C:\Users\doanando\Desktop\atbsch9 - Copy (3).txt
C:\Users\doanando\Desktop\atbsch9 - Copy.txt
C:\Users\doanando\Desktop\atbsch9.txt
'''

# %% Checking Path Validity
# p.exists()  - True if path exists
# p.is_file() - True if path exists and is a file
# p.is_dir()  - True if path exists and is a directory
winDir = Path('C:/Windows')
notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
calcFile = Path('C:/Windows/System32/calc.exe')
winDir.exists() # True
winDir.is_dir() # True
notExistsDir.exists() # False
calcFile.is_file() # True
calcFile.is_dir() # False
# %% You can determine whether a flash drive is currently attached
# to the computer by checking for it with the exists() method
dDrive = Path('D:/')
dDrive.exists() # False

# %% The File Reading/Wrting Process
from pathlib import Path
p = Path('spam.txt')
p.write_text('Hello, world!')
# 13 ( 13 characters were written to the file)
p.read_text()
# 'Hello, world!'

# %% 3 Steps to reading and writing files in Python
# 1. Call the open() fn to return a File object
# 2. Call the read() or write() method on the File object
# %% Opening Files with the open() fn
from pathlib import Path
helloFile = open(Path.home() / 'hello.txt')
helloFile = open('C:\\Users\\doanando\\hello.txt') # same as above
# %% Reading the Content of Files
helloContent = helloFile.read()
helloContent
# 'Hello, world!!!'
sonnetFile = open(Path.home() / 'sonnet29.txt')
sonnetFile.readlines()
'''
["When, in disgrace with fortune and men's eyes,\n",
 'I all alone beweep my outcast state,\n',
 'And trouble deaf heaven with my bootless cries,\n',
 'And look upon myself and curse my fate,']
'''
# note: except the last line of the file,
# each string ends w/ '\n'

# %% Writing to Files
# 'w' write plaintext mode, 'a' append plaintext mode
# if the filename passed to open() does not exist,
#  both write and append mode will create a new, blank file
# after reading or writing to a file, call the close() method
#  before opening the file again (or use 'with open(p) as fileX:')
from pathlib import Path
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, world!\n')
baconFile.close()

with open(Path('bacon.txt'), 'a') as baconFile:
    baconFile.write('Bacon is not a vegetable.')
with open('bacon.txt') as baconFile:
    content = baconFile.read()
print(content)
'''
Hello, world!
Bacon is not a vegetable.
'''
# %% Saving Variables w/ the shelve Module
import shelve
'''
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
'''
with shelve.open('mydata') as shelfFile:
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats
# %% shelf files can read and write once opened
import shelve
with shelve.open('mydata') as shelfFile:
    print(type(shelfFile))
    # <class 'shelve.DbfilenameShelf'>
    print(shelfFile['cats'])
    # ['Zophie', 'Pooka', 'Simon']
# %% since these methods return list-like values instead of true lists,
# you should pass them to the list() fn to get them in list form
with shelve.open('mydata') as shelfFile:
    print(list(shelfFile.keys()))
    # ['cats']
    print(list(shelfFile.values()))
    # [['Zophie', 'Pooka', 'Simon']]

# %% Saving variables w the pprint.pformat() fn
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
# "[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
with open('myCats.py', 'w') as fileObj:
    fileObj.write(f'cats = {pprint.pformat(cats)}\n')
    # 83
# %%
import myCats
myCats.cats
# [{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
myCats.cats[0]
# {'desc': 'chubby', 'name': 'Zophie'}
myCats.cats[0]['name']
# 'Zophie'

# %%
