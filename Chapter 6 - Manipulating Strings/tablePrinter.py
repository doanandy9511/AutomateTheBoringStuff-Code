
def printTable(tableData):
    colWidths = [0] * len(tableData)
    for col in range(len(tableData)):
        for i in tableData[col]:
            if len(i) > colWidths[col]:
                colWidths[col] = len(i)
    
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colWidths[col]+1), end='')
        print()


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)

if __name__ == '__main__':
    main()
