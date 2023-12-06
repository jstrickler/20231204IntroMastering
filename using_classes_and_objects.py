#  list is a class (AKA type)
#  cities is an instance
#  cities.append() is a method (AKA instance method)

cities = list()
cities.append("Dallas")
cities.append("Cleveland")
cities.sort()
cities.insert(0, "Milwaukee")

class Animal:
    def walk(self):   #  'self' is congruent to 'this' in Java
        print("walking...")

class Dog(Animal):
    def bark(self):
        print("woof-woof")

d1 = Dog()
d1.walk()
d1.bark()










