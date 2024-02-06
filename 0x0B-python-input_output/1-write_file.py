#!/usr/bin/python3
'''A module'''


def write_file(filename="", text=""):
    '''A function'''

    with open(filename, 'w', encoding='utf-8') as my_file:
        my_file.write(text)
        return (len(text))
