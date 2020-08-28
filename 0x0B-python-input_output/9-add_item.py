#!/usr/bin/python3
import json
import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file = 'add_item.json'
json_list = []
if os.path.exists(file):
    json_list = load_from_json_file(file)
for ar in sys.argv:
    json_list.append(ar)
save_to_json_file(json_list, file)
