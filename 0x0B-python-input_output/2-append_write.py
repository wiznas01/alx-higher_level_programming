#!/usr/bin/python3
"""Defines a file appending function"""

def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF-8) and returns the number of characters added.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters
