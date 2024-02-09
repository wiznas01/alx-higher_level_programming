#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    Prints an integer value.

    Args:
    - value: The value to be printed, which can be of any type.

    Returns:
    - bool: True if the value is an integer, False otherwise.

    Prints:
    - The integer value followed by a new line if it's an integer.
    - Prints an error message with "Exception:" if value is not an integer

    You have to use try: / except:
    You have to use "{:d}".format() to print as an integer.
    You are not allowed to use type().
    """
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except ValueError as e:
        import sys
        if "'d'" in str(e) and "object of type 'str'" in str(e):
            print("Exception:", e, file=sys.stderr)
        else:
            print("Exception: Not an integer", file=sys.stderr)
        return False
