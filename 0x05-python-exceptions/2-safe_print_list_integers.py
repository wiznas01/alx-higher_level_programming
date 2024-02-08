#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x integers of a list.

    Args:
    - my_list (list): The input list.
    - x (int): The number of elements to access in my_list.

    Returns:
    - int: The real number of integers printed.
    """
    count = 0

    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except (ValueError, TypeError):
        pass
    print()  # Print a new line after all integers are printed
    return count
