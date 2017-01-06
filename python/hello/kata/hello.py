from six.moves import input


def greeting():
    name = input("What is you name? ")
    if name == "Brandon":
        return "Hello, {}, nice to meet you!".format(name)
    elif name == "Brian":
        return "Sup {}!".format(name)
    else:
        return "Hello, {}, I hope you are well.".format(name)


def main():
    print(greeting())


if __name__ == '__main__':
    main()
