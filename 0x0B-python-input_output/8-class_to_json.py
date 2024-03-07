#!/usr/bin/python3
"""Defines a function to return the dictionary description for JSON"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary describing the serializable attributes of object
    """
    return obj.__dict__
