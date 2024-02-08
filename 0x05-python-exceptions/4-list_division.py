#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divide element by element 2 lists.

    Args:
    - my_list_1 (list):first list containing elements of any type.
    - my_list_2 (list): The second list containing elements of any type
    - list_length (int): The length of the resulting list

    Returns:
    - list: A new list with the result of element-wise divisions.

    If 2 elements can’t be divided, the division result should be equal to 0.
    If an element is not an integer or float:
        print: 'wrong type'
    If the division can’t be done (/0):
        print: 'division by 0'
    If my_list_1 or my_list_2 is too short:
        print: 'out of range'

    You have to use try: / except: / finally:
    You are not allowed to import any module.
    """
    result_list = []

    for i in range(list_length):
        try:
            result = 0
            # Check if elements are not integers or floats
            if not (isinstance(my_list_1[i], (int, float)) and
                    isinstance(my_list_2[i], (int, float))):
                raise TypeError("wrong type")

            # Check if the divisor is not zero
            if my_list_2[i] != 0:
                result = my_list_1[i] / my_list_2[i]
            else:
                raise ZeroDivisionError("division by 0")

        except IndexError:
            print("out of range")
        except TypeError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
        finally:
            result_list.append(result)

    return result_list
