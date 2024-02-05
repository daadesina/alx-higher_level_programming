#!/usr/bin/python3
'''A module'''


class BaseGeometry:
    '''A class'''

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')

        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    '''A child class'''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return (f"[{type(self).__name__}] {self.__width}/{self.__height}")


class Square(Rectangle):
    '''A grandchild class'''

    def __init__(self, size):
        self.__size = size

        super().__init__(self.__size, self.__size)

    def __str__(self):
        return (f"[{type(self).__name__}] {self.__size}/{self.__size}")
