#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        value_sort = sorted(a_dictionary.items(), key=lambda kv_pairs:
                            kv_pairs[1])
        return value_sort[-1][0]
    else:
        return None
