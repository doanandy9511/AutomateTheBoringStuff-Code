
myPets = ['Zophie', 'Pooka', 'Fat-tail']

print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named {}'.format(name))
else:
    print('{} is my pet.'.format(name))
