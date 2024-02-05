#!/usr/bin/python3
'''A module'''


def add_attribute(obj, attr, value):
    '''A function'''

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
