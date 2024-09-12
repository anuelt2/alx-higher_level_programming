#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    num_of_names = len(dir(hidden_4))
    name_list = dir(hidden_4)
    sorted_name_list = sorted(name_list)
    i = 0
    while i < num_of_names:
        if (sorted_name_list[i][0] == '_') and (sorted_name_list[i][1] == '_'):
            i += 1
            continue
        print(sorted_name_list[i])
        i += 1
