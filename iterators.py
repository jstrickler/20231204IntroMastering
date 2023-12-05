colors = ["red", "blue", "green", "yellow", "brown", "black", 
          "olive", "pink", "orange", "white", "mauve", "burnt umber"]
months = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
)

rcolors = reversed(colors)
print(f"rcolors: {rcolors}")
colors.append("navy")
colors.append("chartreuse")
colors[3] = "tan"
colors[6] = "beige"
for color in rcolors:
    print(color)
print()

month_colors = zip(months, colors)
print(f"month_colors: {month_colors}")

print(list(month_colors))
print()

for i, month in enumerate(months, 1):
    print(i, month)
print()
print(f"list(enumerate(months)): {list(enumerate(months))}")
print()

for i in range(10):
    print("Python is great! (and sometimes weird)")
print()

#  range(stop)  range(start, stop)  range(start, stop, step)

for i in range(1, 11):
    print(i)
print()

for _ in range(3):  # 0, 1, 2
    print('-' * 60)

#  range(1, 5)    #  1 2 3 4

for i in range(5, 101, 5):
    print(i, end=" ")
print('\n')


