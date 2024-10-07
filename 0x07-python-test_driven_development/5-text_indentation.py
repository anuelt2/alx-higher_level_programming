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

    for delimiter in ".?:":
        text = ((delimiter + "\n\n").join([string.strip(" ") for
                                           string in text.split(delimiter)]))
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
