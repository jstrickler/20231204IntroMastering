#     01234
s1 = "spam\n"
# \n \r \t \b \f
print(len(s1))
s2 = 'spam\n'

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")
print('''Guido's the ex-"BDFL" of Python''')

s3 = r"spam\n"
print(s3)

#  \uXXXX  <= FFFF
# \UXXXXXXXX  > FFFF

print("\U00012000")
print("\U00012001")
print("\U00012002")

a1 = "apple"
a2 = "pie"
a3 = a1 + " " + a2
print(a3)

print("app" in a1)
print("program" in a1)
