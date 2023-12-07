from collections import defaultdict

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fruit_lists = defaultdict(list)

print(f"fruit_lists['x']: {fruit_lists['x']}\n")

for fruit in fruits:
    first_letter = fruit[0]
    fruit_lists[first_letter].append(fruit)

for letter, fruit_list in sorted(fruit_lists.items()):
    print(letter, fruit_list)
print('-' * 60)

def get_none():
    return None

safe_dict = defaultdict(get_none)
safe_dict['NC'] = 'Raleigh'
safe_dict['FL'] = 'Tallahassee'
print(f"safe_dict: {safe_dict}")
print(f"safe_dict['NC']: {safe_dict['NC']}")
print(f"safe_dict['SC']: {safe_dict['SC']}")
print('-' * 60)








