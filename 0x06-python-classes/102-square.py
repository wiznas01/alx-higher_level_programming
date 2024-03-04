#!/usr/bin/python3
"""Module with class Square for square representation"""


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
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public method to calculate the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison method based on area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison method based on area"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison method based on area"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison method based on area"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison method based on area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison method based on area"""
        return self.area() >= other.area()
