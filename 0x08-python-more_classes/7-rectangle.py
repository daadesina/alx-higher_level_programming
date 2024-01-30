#!/usr/bin/python3
"""A module of class
"""


class Rectangle:
    """A class of rectangle
    """

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances = Rectangle.number_of_instances + 1
        Rectangle.print_symbol = self.print_symbol

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        my_area = self.__width * self.__height
        return my_area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            my_per = (2 * self.__width) + (2 * self.__height)
            return my_per

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height - 1):
                for j in range(self.__width):
                    print(self.print_symbol, end="")
                print()
            return str((self.__width * self.print_symbol))

    def __repr__(self):
        return "Rectangle("+str(self.__width)+", "+str(self.__height)+")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
