# Project: Fantasy Game Inventory

def displayInventory(inv):
    total = 0
    print('Inventory:')
    for k,v in inv.items():
        total += v
        print(f'{v} {k}')
    print(f'Total number of items: {total}')

def addToInventory(inv, addedItems):
    for item in addedItems:
        inv.setdefault(item, 0)
        inv[item] += 1
    return inv

def main():
    myInventory = {'rope': 1, 
                   'torch': 6, 
                   'gold coin': 42, 
                   'dagger': 1, 
                   'arrow': 12}
    displayInventory(myInventory)

    print()
    myInventory = {'rope': 1, 
                   'gold coin': 42}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    myInventory = addToInventory(myInventory, dragonLoot)
    displayInventory(myInventory)

if __name__ == '__main__':
    main()
