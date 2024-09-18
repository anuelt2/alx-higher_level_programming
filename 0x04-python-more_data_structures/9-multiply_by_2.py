#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = dict(map(lambda kv_pair: (kv_pair[0], kv_pair[1] * 2),
                              a_dictionary.items()))
    return new_dictionary
