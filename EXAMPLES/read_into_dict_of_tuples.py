from pprint import pprint

FILE_NAME ="../DATA/knights.txt" 

def main():
    hobnob = read_data()
    pretty_print(hobnob)
    print()
    print_titles(hobnob)
    print()

    x = get_field(hobnob, 'Arthur', 1)
    print(f"x: {x}")

def read_data():
    knight_info = {}  # create empty dict

    with open(FILE_NAME) as knights_in:
        for line in knights_in:
            name, title, color, quest, comment = line.rstrip('\n\r').split(":")
            knight_info[name] = title, color, quest, comment  # create new dict element with name as key and a tuple of the other fields as the value
    return knight_info

def pretty_print(data):
    pprint(data)

def print_titles(data):
    for name, info in data.items():
        print(info[0], name)

def get_field(data, knight, field):
    return data[knight][field]

main()






