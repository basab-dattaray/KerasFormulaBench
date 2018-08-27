import os
import json
from pathlib import Path

def get_dict_from_json_file(json_path):
    dict = {}
    file_path = get_abs_path(json_path)
    with open(file_path, 'r') as json_data:
        dict = json.load(json_data)
    return dict

def write_dict_to_file(json_path, dict_in):
    try:
        dict = {}
        file_path = get_abs_path(json_path)
        if os.path.exists(file_path):
            with open(file_path, 'r') as json_file:
                try:
                    dict = json.load(json_file)
                except Exception as e:
                    print(e)

        for k,v in dict_in.items():
            dict[k] = v

        with open(file_path, 'w') as json_file:
            json.dump(dict, json_file, indent=4)
    except Exception as e:
        print(e)

    print('file [] is updated'.format(json_path))



def get_lines_from_file(rel_file_path):
    file_path = get_abs_path(rel_file_path)
    lines = None
    result = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for l in lines:
            l = l.rstrip()
            result.append(l)
    return result


def get_abs_path(json_path):
    try:
        path, file_name = json_path.rsplit('/', 1)
        d = os.getcwd()
        parent_path = Path(d).parent
        folder_path = os.path.join(str(parent_path), path)
        file_path = os.path.join(folder_path, file_name)
    except Exception as e:
        print(e)
    return file_path

