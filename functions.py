
def sqrt(arg):
    if isinstance(arg, (int, float)):
        print(arg ** .5)
    else:
        raise TypeError('Argument must be a number')

sqrt('abc')
sqrt(123)
sqrt([1,2,3])

