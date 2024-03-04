import math

class MagicClass:
    """
    A magical class that performs mystical calculations based on radius.

    Attributes:
    __radius (float): The radius of the magic circle.

    Methods:
    __init__(self, radius=0): Initializes the MagicClass with a given radius.
    area(self): Calculates and returns the area of the magic circle.
    circumference(self): Calculates and returns the circumference of the magic circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of MagicClass.

        Args:
        radius (float): The radius of the magic circle.

        Raises:
        TypeError: If the provided radius is not a number.
        """
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magic circle.

        Returns:
        float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the magic circle.

        Returns:
        float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
