#!/usr/bin/python3
''' Write a function that reads a text file (UTF8) and prints it to stdout '''


def read_file(filename=""):
    '''A function'''

    with open(filename, 'r', encoding='utf-8') as my_file:
        print(my_file.read(), end="")
