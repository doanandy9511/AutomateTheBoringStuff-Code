# Chapter 10 - Organizing Files

# The shutil module
# shutil (shell utilities) module has fn's that let you copy,
#  move, rename, and delete files in your Python programs

# %% Copying files and folders
# shutil.copy(src, dst) will copy the file at the path src to
#  the folder at the path dst
# If dst is a filename, it will be used as the new name of the
#  copied file
import shutil, os
from pathlib import Path
p = Path.home()
with open(p / 'spam.txt', 'a') and open(p / 'eggs.txt', 'a'):
    pass
if not (p / 'some_folder').is_dir():
    os.mkdir(p / 'some_folder')
shutil.copy(p / 'spam.txt', p / 'some_folder')
# 'C:\\Users\\doanando\\some_folder\\spam.txt'
shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')
# WindowsPath('C:/Users/doanando/some_folder/eggs2.txt')

# %% shutil.copy() will copy a single a single file, shutil.copytree()
#     will copy an entire folder and every folder and file contained in it
# shutil.copytree(src, dst) will copy the folder at the path src, along with
#  all of its files and subfolders
import shutil, os
from pathlib import Path
p = Path.home()
shutil.copytree(p / 'spam', p / 'spam_backup')
# WindowsPath('C:/Users/doanando/spam_backup')
# %% Moving and renaming files and folders
import shutil
shutil.move('C:\\Users\\doanando\\bacon.txt', 'C:\\Users\\doanando\\eggs')
# 'C:\\Users\\doanando\\eggs\\bacon.txt'
# if the destination name is not an existing folder, the file will be 
#  saved with that name (no extension)

# %% If a file with the same name exists in the destination folder, 
#  the file will be overwritten
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')

# %% The folders that make up the destination must already exist
shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
# FileNotFoundError: [Errno 2] No such file or directory: 'spam.txt'

# %% Permanently deleting files and folders
# os.unlink(path) will delete the file at path
# os.rmdir(path) will delete the folder at path. This folder must be 
#  empty of any files or folders
# shutil.rmtree(path) will remove the folder at path, and all files and 
#  folders it contains will also be deleted
import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    #os.unlink(filename)
    print(filename)
# test to see which file would be deleted first

# %% Safe deletes with send2trash module
# shutil.rmtree() fn irreversibly deletes files and folders which 
#  can be dangerous to use
# send2trash is much safer bc it will send folders and files to 
#  the recycle bin instead of permanently deleting them
import send2trash
with open('bacon.txt', 'a') as baconFile: # creates the file
    baconFile.write('Bacon is not a vegetable.\n')
send2trash.send2trash('bacon.txt')

# %% Walking a directory tree
# Say you want to rename every file in some folder and also every file
#  in every subfolder of that folder. That is, you want to walk through
#  the directory tree, touching each file as you go.
import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print(f'The current folder is {folderName}')

    for subfolder in subfolders:
        print(f'SUBFOLDER OF {folderName}: {subfolder}')

    for filename in filenames:
        print(f'FILE INSIDE {folderName}: {filename}')

    print('')
'''
The current folder is C:\delicious
SUBFOLDER OF C:\delicious: cats
SUBFOLDER OF C:\delicious: walnut
FILE INSIDE C:\delicious: spam.txt

The current folder is C:\delicious\cats
FILE INSIDE C:\delicious\cats: catnames.txt
FILE INSIDE C:\delicious\cats: zophie.jpg

The current folder is C:\delicious\walnut
SUBFOLDER OF C:\delicious\walnut: waffles

The current folder is C:\delicious\walnut\waffles
FILE INSIDE C:\delicious\walnut\waffles: butter.txt
'''

# %% Compressing files with the zipfile module

