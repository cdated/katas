from __future__ import print_function
from six.moves import input
import re


def read_quotes():
    data = input('Enter quotes and authors in the format ("quote0" author0) ("quote1" author1):\n')

    return data

def parse_quotes(data):
    quotes_data = {}

    regex = r'\("([\w\d\s\.\?\']+)" ([\w\s\.]+)\)'
    for match in re.findall(regex, data):
        quote, author = match
        quotes_data[author] = quote

    return quotes_data

def main():
    quote_data = parse_quotes(read_quotes())

    for author in sorted(quote_data):
        print('{} says, "{}"'.format(author, quote_data[author]))

if __name__ == '__main__':
    main()
