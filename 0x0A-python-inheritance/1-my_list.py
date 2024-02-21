#!/usr/bin/python3

class MyList(list):
    """
    MyList class inherits from list and adds a print_sorted method.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
