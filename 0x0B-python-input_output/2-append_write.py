#!/usr/bin/python3
'''A module'''


def append_write(filename="", text=""):
    '''A function'''

    with open(filename, 'a', encoding='utf-8') as my_file:
        my_file.write(text)
        return (len(text))
