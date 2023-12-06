from pprint import pprint
import logging    # logging is a module 
import sys

FILE_NAME ="../DATA/xknights.txt" 

def main():
    logging.basicConfig(
        filename="knightinfo.log",
        level=logging.DEBUG,
    )
    logging.info("program starts")
    try:
        hobnob = read_data()
    except OSError as err:
        print("ending program")
        exit()
    pretty_print(hobnob)
    print()
    print_titles(hobnob)
    print()

    x = get_field(hobnob, 'Arthur', 1)
    print(f"x: {x}")
    logging.info("program ends")

def read_data():
    knight_info = {}  # create empty dict
    logging.debug("data file name is %s", FILE_NAME)
    try:
        with open(FILE_NAME) as knights_in:
            for line in knights_in:
                logging.debug("raw record: %s", line.rstrip())
                name, title, color, quest, comment = line.rstrip('\n\r').split(":")
                knight_info[name] = title, color, quest, comment  # create new dict element with name as key and a tuple of the other fields as the value
    except OSError as err:
        logging.exception("Unable to read file %s", FILE_NAME)
        raise
    return knight_info

def pretty_print(data):
    pprint(data)

def print_titles(data):
    for name, info in data.items():
        print(info[0], name)

def get_field(data, knight, field):
    return data[knight][field]

main()






