#!/usr/bin/python3
"""A module of function"""


def text_indentation(text):
    """A function of text"""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for i in range(len(text)):
        if text[i - 1] == '.' and text[i] == ' ':
            print()
            print()
            continue
        elif text[i - 1] == '?' and text[i] == ' ':
            print()
            print()
            continue
        elif text[i - 1] == ':' and text[i] == ' ':
            print()
            print()
            continue

        print(text[i], end="")
    print()
    print()
