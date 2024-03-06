#!/usr/bin/python3
"""Defines a file writing function"""


def write_file(filename="", text=""):
    """
    Writes string to a text file and returns number of characters written.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters
