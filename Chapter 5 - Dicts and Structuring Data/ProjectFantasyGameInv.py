# Project: Fantasy Game Inventory

def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for k,v in inventory.items():
        total += v
        print(f'{v} {k}')
    print(f'Total number of items: {total}')

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    pass

def main():
    myInventory = {'rope': 1, 
                   'torch': 6, 
                   'gold coin': 42, 
                   'dagger': 1, 
                   'arrow': 12}
    displayInventory(myInventory)

if __name__ == '__main__':
    main()
