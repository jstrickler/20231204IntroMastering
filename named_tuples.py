from collections import namedtuple
from pprint import pprint

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

Person = namedtuple('Person', 'first_name last_name product dob')

people_tuples = []
for first_name, last_name, product, dob in people:
    people_tuples.append(Person(first_name=first_name, last_name=last_name, product=product, dob=dob))


def process_people(people_list):
    for person in people_list:
        print(person.first_name, person.last_name)


process_people(people_tuples)


Point = namedtuple('Point', 'x y')

p = Point(12, 10)
print(p)
print(p.x, p.y)
print('-' * 60)

pprint(people_tuples)



