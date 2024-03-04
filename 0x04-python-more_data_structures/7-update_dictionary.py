#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))


if __name__ == "__main__":
    def update_and_print(original_dict, key, value):
        new_dict = update_dictionary(original_dict, key, value)
        print_sorted_dictionary(new_dict)
        print("--")
        print_sorted_dictionary(original_dict)
        print("--")
        print("--")

    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    update_and_print(a_dictionary, 'language', "Python")

    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    update_and_print(a_dictionary, 'city', "San Francisco")
