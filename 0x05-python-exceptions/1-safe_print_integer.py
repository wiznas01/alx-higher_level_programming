#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
    - value: The input value.

    Returns:
    -bool: True if value is integer and correctly printed, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
