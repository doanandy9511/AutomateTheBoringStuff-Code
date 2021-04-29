# %%
while True:
    age = input('Enter your age: ')
    try:
        age = int(age)
    except Exception:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break
print(f'Your age is {age}.')

# %%
import pyinputplus