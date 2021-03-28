
catNames = []
while True:
    print('Enter the name of cat {0} (Or enter nothing to stop.):'.format(len(catNames)+1))
    name = input()
    if name == '':
        break
    catNames.append(name)
print('The cat names are:')
for name in catNames:
    print(' ' + name)