import re, sys
from pathlib import Path

def main():
    if len(sys.argv) > 2:
        directory = Path(sys.argv[1])
        if directory.is_dir():
            print('woohoo')
            print(directory.name)
        regex = sys.argv[2]
    else:
        print('BOOO, not enough parameters.')
    
if __name__ == '__main__':
    main()