#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = list(map(lambda element: replace if element == search
                           else element, my_list))
    return my_new_list
