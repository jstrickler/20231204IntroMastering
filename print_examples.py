city = "Pittsburgh"
person = "Rocky Balboa"
amount = 37.329034

print(city, person, amount)  # print(str(city) + " " + str(person) + " " + str(amount) + "\n")
print("xxx")

print(city, person, amount, sep="/")
print(city, person, amount, sep="##")

print(city, end=" ")

print(person)

s = "spam\n"
print(s)
print('---')
print(s, end="")
print('---')
print()

#  CITY:PERSON
print(city + ":" + person)
print(f"{city}:{person}")  #   f string --   f"{expr} other stuff {expr} other stuff ...."
print(f"Amount is {amount}")
print(f"Amount is {amount:.2f}")  # f strings added with 3.6

print("{}:{}".format(city, person))
print("Amount is {:.2f}".format(amount))


















