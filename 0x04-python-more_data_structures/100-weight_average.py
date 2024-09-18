#!/usr/bin/python3
def weight_average(my_list=[]):
    length = len(my_list)
    if len(my_list) == 0:
        return 0
    weighted_scores = list(map(lambda values: values[0] * values[1], my_list))
    sum_of_weighted_scores = sum(weighted_scores)
    weights = list(map(lambda values: values[1], my_list))
    sum_of_weights = sum(weights)
    weighted_average = sum_of_weighted_scores / sum_of_weights
    return weighted_average
