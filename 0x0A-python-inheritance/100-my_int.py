#!/usr/bin/python3
'''A module'''


class MyInt(int):
    '''A class'''

    def __eq__(self, value):
        return int(self) != value

    def __ne__(self, value):
        return int(self) == value
