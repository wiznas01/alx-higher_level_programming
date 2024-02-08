#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints the first x elements of a list.

    Args:
    - my_list (list): The input list.
    - x (int): The number of elements to print.

    Returns:
    - int: The real number of elements printed.
    """
    count = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()  # Print a new line after all elements are printed
        return count
