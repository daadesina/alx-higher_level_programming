#!/usr/bin/python3
'''A module'''


from models.base import Base


class Rectangle(Base):
    '''A class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif type(height) is not int:
            raise TypeError('height must be an integer')
        elif type(x) is not int:
            raise TypeError('x must be an integer')
        elif type(y) is not int:
            raise TypeError('y must be an integer')

        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise ValueError('height must be > 0')
        elif x < 0:
            raise ValueError('x must be >= 0')
        elif y < 0:
            raise ValueError('y must be >= 0')

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        return (self.__height * self.__width)

    def display(self):
        for i in range(self.__height - 1):
            for j in range(self.__width):
                print('#', end="")
            print()
        print(self.__width * '#')

    def __str__(self):
        return (f'[{type(self).__name__}] '
                + f'({self.id}) {self.__x}/{self.__y} - '
                + f'{self.__width}/{self.__height}')

    def display(self):
        if (self.__y != 0):
            for i in range(self.__y):
                print()
        for i in range(self.__height):
            print((self.__x) * " ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):

        myList = []
        for i in args:
            myList = myList + [i, ]

        if len(myList) == 1:
            self.id = myList[0]

        if len(myList) == 2:
            self.id = myList[0]
            self.__width = myList[1]

        if len(myList) == 3:
            self.id = myList[0]
            self.__width = myList[1]
            self.__height = myList[2]

        if len(myList) == 4:
            self.id = myList[0]
            self.__width = myList[1]
            self.__height = myList[2]
            self.__x = myList[3]

        if len(myList) == 5:
            self.id == myList[0]
            self.__width = myList[1]
            self.__height = myList[2]
            self.__x = myList[3]
            self.__y = myList[4]

        iList = []
        for i, j in kwargs.items():
            iList = iList + [i, j]

        for n in range(len(iList)):
            if iList[n - 1] == "height":
                self.__height = iList[n]
            elif iList[n - 1] == "width":
                self.__width = iList[n]
            elif iList[n - 1] == "x":
                self.__x = iList[n]
            elif iList[n - 1] == "y":
                self.__y = iList[n]
            elif iList[n - 1] == "id":
                self.id = iList[n]
