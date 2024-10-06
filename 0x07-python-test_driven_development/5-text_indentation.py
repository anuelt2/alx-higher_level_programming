#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """A function that prints a text with 2 new lines after some characters.

    Args:
        text: text to be printed.

    Raises:
        TypeError: If text is not str.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{}".format(text[i]))
            i += 1
            print()
        else:
            print("{}".format(text[i]), end="")
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
