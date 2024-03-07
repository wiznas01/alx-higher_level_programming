#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise, returns False.

    Args:
        obj (object): The object to check.
        a_class (class): The specified class to compare against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
