#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
     from the specified class; otherwise, returns False.

    Args:
        obj (object): The object to check.
        a_class (class): The specified class to compare against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
