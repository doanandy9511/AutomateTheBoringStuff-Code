import re, sys
from pathlib import Path

def main():
    if len(sys.argv) > 2:
        directory = Path(sys.argv[1])
        regex = sys.argv[2]
        searchRe = re.compile(regex)
        if directory.is_dir():
            for file in list(directory.glob('*.txt')):
                with open(file) as file:
                    lines = file.readlines()
                    for line in lines:
                        if searchRe.search(line) != None:
                            print(line.strip())
    else:
        print('BOOO, not enough parameters.')
    
if __name__ == '__main__':
    main()