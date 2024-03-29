#!/usr/bin/python3

def weight_average(my_list):
    if not my_list or not isinstance(my_list, list):
        return 0

    total_weighted_sum = 0
    total_weights = 0

    for score, weight in my_list:
        total_weighted_sum += score * weight
        total_weights += weight

    if total_weights == 0:
        return 0

    return total_weighted_sum / total_weights
