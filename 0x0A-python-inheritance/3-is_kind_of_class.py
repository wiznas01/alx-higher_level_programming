#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class; otherwise,
    returns False.

    Returns:
        bool: True if obj is an instance of a_class or its subclass, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
