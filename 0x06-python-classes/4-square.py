#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'

"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'

    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__val

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__val = value

    def area(self):
        s = self.__val * self.__val
        return s
