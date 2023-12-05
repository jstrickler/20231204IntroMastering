d1 = dict()  # empty dict

d2 = {'m': 4, 'j': 19, 'a': 7}

months = {'Jan': 31, 'Feb': 28, 'Mar': 31,}

d3 = {}  # empty dict

for name, number_of_days in months.items():  # same order items were added
    print(name, number_of_days)
print()

months['Apr'] = 30
months['Oct'] = 31
print(f"months: {months}")
months['Feb'] = 29
print(f"months: {months}")

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"airports['YCC']: {airports['YCC']}")
print(f"airports['MCO']: {airports['MCO']}")
print()

# print(f"airports['MIA']: {airports['MIA']}")

print(f"airports.get('RDU'): {airports.get('RDU')}")
print(f"airports.get('MIA'): {airports.get('MIA')}")
print(f"airports.get('MIA', 'not found'): {airports.get('MIA', 'not found')}")
print()

print(f"airports.setdefault('MIA', 'Miami'): {airports.setdefault('MIA', 'Miami')}")
print()

print(f"airports: {airports}")
print()

for code in 'RDU', 'XYZ', 'Wombat', 'YCO', 'MIA':
    print(code, code in airports)
print()

for kv in airports.items():
    print(kv)
print()

#    key  value
for code, city in airports.items():
    print(f"{code}: {city}")

print(f"airports.keys(): {airports.keys()}")
print()
print(f"airports.values(): {airports.values()}\n")

