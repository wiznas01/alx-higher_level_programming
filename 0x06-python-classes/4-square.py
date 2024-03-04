#!/usr/bin/python3
"""Module with a class Square that defines a square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialization method for the Square class"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public method to calculate the area of the square"""
        return self.__size ** 2
