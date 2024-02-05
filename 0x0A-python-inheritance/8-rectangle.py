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

        super().integer_validator("width", width)
        super().integer_validator("height", height)
