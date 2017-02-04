from __future__ import print_function
from six.moves import input


TEMPLATE = """A boy and his mother went to the store to buy a \
{noun} they needed one that was {adjective}. However, they would have \
to {verb} {adverb}."""


def get_answers():
    """ Get users responses as dict """

    values = dict()
    values["noun"] = input('Enter a noun: ')
    values["verb"] = input('Enter a verb: ')
    values["adjective"] = input('Enter a adjective: ')
    values["adverb"] = input('Enter a adverb: ')

    return values


def main():

    response = TEMPLATE.format(**get_answers())
    print(response)


if __name__ == '__main__':
    main()
