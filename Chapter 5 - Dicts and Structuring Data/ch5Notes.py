# %% The Dictionary Data Type
# Dictionaries are mutable collections of many values.
# They use keys to reference their values.
# A key with its associate value is called a key-value pair.
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# %%
myCat['size']
# %%
f"My cat has {myCat['color']} fur."
# %% Dictionaries vs. Lists
# order does not matter for comparing two dicts
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon
# %%
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham
# %% the keys(), values(), and items() methods
# values returned by these are not true lists:
#  they cannot be modified and do not have an append() method
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

# %%
for v in spam.keys():
    print(v)
# %%
for k,v in spam.items():
    print(f'{k}: {v}')
# %%
spam = {'color': 'red', 'age': 42}
spam.keys()
# dict_keys(['color', 'age'])
list(spam.keys())
# ['color', 'age']

# %% Checking Whether a Key or Value Exists in a Dictionary
spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys()
# True
# %%
'Zophie' in spam.values()
# True
# %%
'color' not in spam.keys()
# True
# %% same as 'color' in spam.keys()
'color' in spam

# %% the get() method
# my_dict.get(key_value, fallback_value)
picnicItems = {'apples': 5, 'cups': 2}
f"I am bringing {picnicItems.get('cups', 0)} cups."
# %%
f"I am bringing {picnicItems.get('eggs', 0)} eggs."

# %% the setdefault() method
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
spam
# %%
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color','black')
# 'black'
spam
# %%
spam.setdefault('color', 'white')
# 'black'
spam
# %% pretty printing, character count
# %% tic-tac-toe board

# %% Nest Dictionaries and Lists

