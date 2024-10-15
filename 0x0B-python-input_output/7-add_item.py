#!/usr/bin/python3
"""A module for a script that adds all arguments
to a Python list, and saves them to a file.
"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []

if path.exists('add_item.json'):
    my_list = load_from_json_file('add_item.json')

for i in range(len(argv)):
    if i == 0:
        continue
    my_list.append(argv[i])

save_to_json_file(my_list, 'add_item.json')
