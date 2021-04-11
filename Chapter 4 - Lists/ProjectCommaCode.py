
# %%

def printList(l = None):
    if l is None:
        print('No list was passed.')
        return
    if l == []:
        print('Empty list passed.')
        return
    elif len(l) > 0:
        print(l, sep=',')
    

def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    printList(spam)

if __name__ == '__main__':
    main()
# %%
