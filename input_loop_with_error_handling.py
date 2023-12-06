while True:
    raw_number = input("Enter a number: ")
    try:
        number = float(raw_number)
    except ValueError as err:
        print("Invalid number")
        continue
    else:
        break
