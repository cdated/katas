from __future__ import print_function
from six.moves import input


def get_input():
    data = input('')
    try:
        data = float(data)
        return data
    except ValueError:
        print('Value provided is not numeric')


def main():
    print(get_input())


if __name__ == '__main__':
    main()
