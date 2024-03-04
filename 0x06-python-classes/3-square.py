#!/usr/bin/python3
"""Module with a class Square that defines a square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialization method for the Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public method to calculate the area of the square"""
        return self.__size ** 2
