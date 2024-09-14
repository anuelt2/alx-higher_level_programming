#!/usr/bin/python3
def multiple_returns(sentence):
    idx_0 = len(sentence)
    if idx_0 == 0:
        idx_1 = None
    else:
        idx_1 = sentence[0]
    my_tuple = (idx_0, idx_1)
    return my_tuple
