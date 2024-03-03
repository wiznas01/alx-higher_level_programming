#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_sum = 0
    seen_numbers = set()


    for number in my_list:
        if number not in seen_numbers:
            unique_sum += number
            seen_numbers.add(number)

    return unique_sum

if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))

