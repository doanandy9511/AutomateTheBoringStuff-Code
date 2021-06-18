# backupToZip.py - Copies an entire folder and its contents
#  into a ZIP file whose filename increments

import zipfile, os

def backupToZip(folder):
    # back up the entire contens of "folder" into a ZIP file
    folder = os.path.abspath(folder) # make sure folder is absolute
    # figure out the filename this code should use based on
    #  which files already exist
    number = 1
    while True:
        zipFilename = f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    with zipfile.ZipFile(zipFilename, 'w') as backupZip:
        print(f'Creating {zipFilename}...')

        # walk the entire folder tree and compress the files in each folder
        for foldername, subfolders, filenames in os.walk(folder):
            print(f'Adding files in {foldername}...')
            # add the current folder to the ZIP file
            backupZip.write(foldername)

            # add all the files in this folder to the ZIP file
            for filename in filenames:
                newBase = f'{os.path.basename(folder)}_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue # don't back up the backup ZIP files
                backupZip.write(os.path.join(foldername,filename))
    print('Done.')

def main():
    backupToZip(r'C:\Users\doanando\Documents\GitHub\AutomateTheBoringStuff-Code')
    backupToZip(r'C:\delicious')

if __name__ == '__main__':
    main()