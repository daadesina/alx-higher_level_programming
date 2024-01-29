#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'

"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'

    """

    def __init__(self, size=0):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

        """

        self.__size = size

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
