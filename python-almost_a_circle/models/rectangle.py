#!/usr/bin/python3
"""
rectangle module that defines the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer for Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """method to calculate area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """method to display a rectangle using #"""
        print("\n" * (self.__y), end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """return string representation of Rectangle"""
        return '[' + type(self).__name__ + '] (' + str(self.id) \
            + ') ' + str(self.__x) + '/' + str(self.__y) + ' - ' \
            + str(self.__width) + '/' + str(self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        key = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, key[i], args[i])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns dictionary representation of
        Rectangle instance
        """
        selfDict = {
            'x': self.x,


