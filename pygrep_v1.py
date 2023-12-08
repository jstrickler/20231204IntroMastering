import sys
import fileinput
import re
from argparse import ArgumentParser

parser = ArgumentParser(description="Faux Grep")
parser.add_argument("-i", help="ignore case", action="store_true", dest="ignore_case")
parser.add_argument("-f", help="show file name", action="store_true", dest="show_name")
parser.add_argument("search_term", help="search term")
parser.add_argument("files", nargs="*", help="Files to search (or none for STDIN)")

args = parser.parse_args()

re_flags = 0
if args.ignore_case:
    re_flags |= re.IGNORECASE

rx_search_term = re.compile(args.search_term, re_flags)

for raw_line in fileinput.input(args.files):
    if rx_search_term.search(raw_line):
        if args.show_name:
            print(fileinput.filename(), end=" ")
        print(raw_line.rstrip())

