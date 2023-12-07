
from collections import Counter

with open("../DATA/breakfast.txt") as breakfast_in:
    foods = [line.rstrip() for line in breakfast_in]  # create list of foods with EOL removed from line

counts = Counter(foods)  # initialize Counter object with list of foods
counts['ragu toscano'] += 1
counts['haggis'] += 1

for item, count in counts.items():  # iterate over results
    print(item, count)

