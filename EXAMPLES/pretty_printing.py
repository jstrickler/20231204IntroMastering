from pprint import pprint

struct = {  # nested data structure
    'part1': [
        ['a', 'b', 'c'], ['d', 'e', 'f']
    ],
    'part2': {
        'red': 55,
        'blue': [8, 98, -3],
        'purple': ['Chicago', 'New York', 'L.A.'],
    },
    'part3': ['g', 'h', 'i'],
}

print('Without pprint:')
print(struct)  # print normally
print()

print('With pprint:')
pprint(struct)  # pretty-print
print()

print('With pprint (depth=2):')
pprint(struct, depth=2)  # only print top two levels of structure
print()
print('-' * 60)

d2 = {'m': 4, 'j': 19, 'a': 7}

pprint(d2)
print()

pprint(d2, sort_dicts=False)
print()


