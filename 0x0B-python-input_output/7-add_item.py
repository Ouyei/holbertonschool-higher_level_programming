#!/usr/bin/python3
# 7-add_item.py
# Oscar Bedat <3961@holbertonschool.com>
"""
script that adds all arguments 2 a Python list,
and then save them 2 a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
for i in sys.argv[1:]:
    items.append(i)
save_to_json_file(items, "add_item.json")
