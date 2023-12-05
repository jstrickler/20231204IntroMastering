import sys   # load the sys module

print(f"sys.argv: {sys.argv}\n")

print(f"(script name) sys.argv[0]: {sys.argv[0]}\n")

print(f"sys.argv[1]: {sys.argv[1]}\n")
# print(f"sys.argv[2]: {sys.argv[2]}\n")

raw_c = sys.argv[1]
celsius = float(raw_c)

