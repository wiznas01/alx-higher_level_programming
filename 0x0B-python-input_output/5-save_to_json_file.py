#!/usr/bin/python3
"""Defines a function to save an object to a JSON file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be saved to the JSON file.
        filename (str): The name of the JSON file.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
