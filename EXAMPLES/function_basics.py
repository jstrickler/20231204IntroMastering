

# void function
def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None

def spam():
    pass  # do-nothing statement

x = spam()

say_hello()  # Call function (arguments, if any, in () )


def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()


def sqrt(num):  # Function takes exactly one argument
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(num=2)  # using name is OK

print("m is {:.3f} n is {:.3f}".format(m, n))

# positional-only   (can't use param name)
# positional    (pass by position, but CAN use name, required) 
# optional positional (pass any number of args) (only one)
# named  (pass by name only, required)
# optional named (pass any number of named arguments)

def never_happen(p1, /, p2, p3, *p4, p5, p6, **p7):
    #  p4 is tuple
    #  p7 is dictionary
    pass

never_happen('a', 'b', 'c', 'd', 'e', 'f', p5='g', p6='h', animal="wombat",
             ice_cream="butter pecan")

def f1(p1, p2): pass

def f2(p1, *opt): pass

def f3(p1, *, foo, bar): pass

def find_lines(search_term, *file_paths, ignore_case=False):
    if ignore_case:
        search_term = search_term.lower()
    for file_path in file_paths:
        with open(file_path) as file_in:
            for line in file_in:
                if ignore_case:
                    search_line = line.lower()
                else:
                    search_line = line
                if search_term in search_line:
                    print(line.rstrip())

find_lines('lizard', '../DATA/alice.txt', '../DATA/words.txt', ignore_case=True)


