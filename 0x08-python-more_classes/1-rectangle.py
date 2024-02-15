#!/usr/bin/python3

class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Parameters:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Parameters:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        self._validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Parameters:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        self._validate_dimension(value, "height")
        self.__height = value

    def _validate_dimension(self, value, dimension_name):
        """
        Validate the dimension value.

        Parameters:
            value (int): The dimension value.
            dimension_name (str): The name of the dimension.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{dimension_name} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension_name} must be >= 0")

