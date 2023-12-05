i = 0
while i < 3:
    print(i)
    i += 1   #  i = i + 1

while True:  # loop until break
    file_name = input("Enter file name: ")
    if file_name == 'q':
        break  # exit loop
    if file_name == '':
        print("please enter a file name")
        continue  # go back to top
    print(f"Processing {file_name}")