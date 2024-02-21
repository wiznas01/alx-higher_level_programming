#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: List of strings representing attributes and methods.
    """
    return [item for item in dir(obj)]
