#!/usr/bin/python3
"""A module of print sorted"""


class MyList(list):
    """ A class of my list"""

    def print_sorted(self):
        print(sorted(list(self)))
