#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))


if __name__ == "__main__":
    def delete_and_print(original_dict, key):
        new_dict = simple_delete(original_dict, key)
        print_sorted_dictionary(original_dict)
        print("--")
        print_sorted_dictionary(new_dict)
        print("--")
        print("--")

    a_dictionary = {'language': "C", 'Number': 89,
                    'track': "Low", 'ids': [1, 2, 3]}
    delete_and_print(a_dictionary, 'track')

    a_dictionary = {'language': "C", 'Number': 89,
                    'track': "Low", 'ids': [1, 2, 3]}
    delete_and_print(a_dictionary, 'c_is_fun')
