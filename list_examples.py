list1 = list()   # create new empty list
list2 = []  # same
cities = ['Durham', 'Vancouver', 'Omaha', 'Pittsburgh']

print(len(cities))
print(cities[0], cities[2])

cities.insert(0, "Los Angeles")
print(f"cities: {cities}")
cities.insert(3, "Reno")
print(f"cities: {cities}")
# cities.insert(99, "Miami")
cities.append("Miami")  # adds at end
print(f"cities: {cities}")

more_cities = ["Houston", "New Orleans", "Jacksonville"]

cities.extend(more_cities)
print(f"cities: {cities}")

# LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)
del cities[2]
print(f"cities: {cities}")

cities.remove('Pittsburgh')
print(f"cities: {cities}")
print()

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}")

city = cities.pop(1)
print(f"city: {city}")
print(f"cities: {cities}")

# del LIST[pos]   LIST.remove(value)    LIST.pop()  LIST.pop(pos)

cities.reverse()
print(f"cities: {cities}")
cities.sort()
print(f"cities: {cities}")

print(f"cities.index('Omaha'): {cities.index('Omaha')}")
print(f"cities.count('Omaha'): {cities.count('Omaha')}")

print(f"cities[4]: {cities[4]}")
print(f"cities[0]: {cities[0]}")
print(f"cities[-1]: {cities[-1]}")

# print(f"cities[9]: {cities[9]}")

print(f"cities: {cities}")
print(f"cities[0:3]: {cities[0:3]}")

#  [inclusive-start:exclusive-stop]

print(f"cities[2:4]: {cities[2:4]}")

print(f"cities[:4]: {cities[:4]}")
print(f"cities[3:]: {cities[3:]}")
print(f"cities[1:-1]: {cities[1:-1]}")

s = "'wombat'"
print(f"s: {s}")

s2 = s[1:-1]
print(f"s2: {s2}")

#  sys.argv[1:]  # all args except script name
#  for arg in sys.argv[1:]:
#      ...

city = "New Orleans"
print(f"city[:3]: {city[:3]}")
print(f"city[6:10]: {city[6:10]}")
print()
print(f"cities: {cities}\n")

# for VAR ... in ITERABLE:
#     use VAR ...
for city in cities:
    # city = cities[0]
    # city = cities[1]
    # ...
    print(city)
print()

for letter in s2:
    print(letter)
print()

x = [['a', 5], ['m', 4], ['c', 17], ['e'], ['r', 8, 9, 10], [1, 2, 3]]

for item in x:
    print(item)
print()

#    first, *rest
for letter, *number in x:  # unpack each item into (letter, number)
    print(letter, number)  # number is a list
print()

values = ['a', 'b', 'c', 'd', 'e', 'f']

v1, v2, *v3 = values
print(v1, v2, v3)

v1, *v2, v3 = values
print(v1, v2, v3)

*v1, v2, v3 = values
print(v1, v2, v3)
print()

data = [
    [[1,2], [3,4]],
    [[5,6],[7,8]],
]
for [a,b],[c,d] in data:
    print(a,b,c,d)
    