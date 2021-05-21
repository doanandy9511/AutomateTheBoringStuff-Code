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

