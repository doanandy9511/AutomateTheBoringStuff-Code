import pyinputplus as pyip

def boolYesNo(x):
    return x == 'yes'

def main():
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True, 
                           prompt='Please select a bread type:\n')
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True,
                             prompt='Please select a protein type:\n')
    cheese_ = pyip.inputYesNo('Would you like cheese?\n')
    cheese_ = boolYesNo(cheese_)
    if(cheese_):
        cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True,
                                prompt='Please select a cheese type:\n')
    mayo = pyip.inputYesNo('Would you like mayo?\n')
    mayo = boolYesNo(mayo)
    mustard = pyip.inputYesNo('Would you like mustard?\n')
    mustard = boolYesNo(mustard)
    lettuce = pyip.inputYesNo('Would you like lettuce?\n')
    lettuce = boolYesNo(lettuce)
    tomato = pyip.inputYesNo('Would you like tomato?\n')
    tomato = boolYesNo(tomato)
    quantity = pyip.inputInt('How many sandwiches would you like?\n', min=1)

    price = (5 + (0.5 if cheese else 0) + (0.25 if mayo else 0) + \
            (0.25 if mustard else 0) + (0.1 if lettuce else 0) + \
            (0.1 if tomato else 0)) * quantity

    t = '  '
    n = '\n'
    b = '\b'
    print(
f'''Your order is:
{quantity} Sandwich{'es' if quantity > 1 else ''}:
Bread:{n}{t}{bread}
Protein:{n}{t}{protein}
{f'Cheese:{n}{t}{cheese}' if cheese_ else ''}
Additional:{f'{n}{t}mayo' if mayo else b}{f'{n}{t}mustard' if mustard else b}{f'{n}{t}lettuce' if lettuce else b}{f'{n}{t}tomato' if tomato else b}
Price: ${price:.2f}''')

if __name__ == '__main__':
    main()