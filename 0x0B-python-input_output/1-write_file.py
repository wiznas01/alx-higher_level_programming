#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of characters written.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters

if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
