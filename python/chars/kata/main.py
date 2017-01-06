from six.moves import input


def num_chars():
    word = input("What is the input string? ")
    if word == "":
        return "A string must be provided."

    return "{} has {} characters.".format(word, len(word))


def main():
    print(num_chars())


if __name__ == '__main__':
    main()
