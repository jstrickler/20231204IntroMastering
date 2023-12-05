fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fruit_lists = {}

for fruit in fruits:
    first_letter = fruit[0]
    if first_letter not in fruit_lists:
        fruit_lists[first_letter] = list()
    fruit_lists[first_letter].append(fruit)

for letter, fruit_list in sorted(fruit_lists.items()):
    print(letter, fruit_list)
