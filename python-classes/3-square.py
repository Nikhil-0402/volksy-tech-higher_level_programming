#!/usr/bin/python3
"""This is bad"""


class Square:
    """A class """
    def __init(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size= size

    def arear(self):
        return self.__size *  self.__size
