# deleteUnneededFiles.py - walks through folder tree of hard drive
#  and searches for 
import os
from pathlib import Path

def scanDrive(drive):
    for foldername, subfolders, filenames in os.walk(drive):
        for filename in filenames:
            filename = Path(foldername) / filename
            size = os.path.getsize(filename)
            sizeMB = size // (2**20)
            sizeGB = sizeMB / 1024

            if sizeGB >= 1:
                print(f'{foldername}\\{filename} : {sizeGB:.2f} GB')
            elif sizeMB > 100:
                print(f'{foldername}\\{filename} : {sizeMB} MB')

def main():
    scanDrive('C:\\')

if __name__ == '__main__':
    main()