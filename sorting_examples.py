fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

#  str.lower 
x = "ABC"
print(f"str.lower(x): {str.lower(x)}")

f1 = sorted(fruits, key=str.lower)
print(f"f1: {f1}\n")

# len
f2 = sorted(fruits, key=len)
print(f"f2: {f2}\n")

def len_and_name(item):
    comparison_value = len(item), item.lower()
#    print(f"Comparing {item} as {comparison_value}")
    return comparison_value

f3 = sorted(fruits, key=len_and_name)
print(f"f3: {f3}\n")

#   [[x, y, z], [x, y, z], [x, y, z]]

def by_last_letter(item):
    return item[-1]  # return last letter of each item

f4 = sorted(fruits, key=by_last_letter)
print(f"f4: {f4}\n")

f5 = sorted(fruits, key=lambda e: e[-1])
print(f"f5: {f5}\n")

#  lambda params ...: (return-value)

fruits.sort(key=str.lower)
print(f"fruits: {fruits}\n")

