#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'

"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'

    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__pos

    @position.setter
    def position(self, value):
        if (len(value) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(value[0], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__pos = value

    def area(self):
        s = self.__val * self.__val
        return s

    def my_print(self):
        if self.__val == 0:
            print()
        else:
            for i in range(self.__val):
                if self.__pos[1] >= 0:
                    print("_" * self.__pos[0], end="")
                    print("#" * self.__val)
                else:
                    print("#" * self.__val)
