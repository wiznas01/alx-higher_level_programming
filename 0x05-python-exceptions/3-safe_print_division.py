#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
    - a (int): The numerator.
    - b (int): The denominator.

    Returns:
    - float or None: The result of the division or None if an exception occurs
    """
    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    except TypeError:
        print("Inside result: None")
        return None
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
            return result
