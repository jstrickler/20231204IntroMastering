from collections import Counter

with open('DATA/breakfast.txt') as breakfast_in:
    foods = breakfast_in.read().splitlines() 

# print(f"foods: {foods}")

counts = Counter(foods)

counts['eggs benedict'] += 1

print(f"counts: {counts}\n")

print(f"counts.most_common(3): {counts.most_common(3)}")
