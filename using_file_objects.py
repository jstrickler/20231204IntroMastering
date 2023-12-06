with open('DATA/fruit.txt') as fruits_in:
    fruits = fruits_in.read().splitlines()
    # fruits = [f.rstrip() for f in fruits_in]

    print(f"sorted(fruits): {sorted(fruits)}\n")
    
    print(f"sorted(fruits, key=str.lower): {sorted(fruits, key=str.lower)}\n")

print(f"len(fruits): {len(fruits)}")

try:
    print(fruits[22])  # run-time error
    print("ok")
except IndexError as err:
    print(err)


