import os
import json
from pathlib import Path
import shutil
import datetime

def remove_file(file_path):
    if file_path is None:
        return
    path = get_abs_path(file_path)
    if path is not None:
        if os.path.exists(path):
            os.remove(path)

def remove_directory_tree(dir_path):
    path = get_abs_path(dir_path)
    if os.path.exists(path):
        shutil.rmtree(path)

def get_filename_based_on_time():
    s = str(datetime.datetime.now())
    fname = s.replace(':', '-')
    return fname

def get_file_modification_datetime(filename_path):
    filepath = get_abs_path(filename_path)
    t = os.path.getmtime(filepath)
    return datetime.datetime.fromtimestamp(t)

def move_and_override_file(src_file_path, dst_dir_path, src_file_name):
    src_file_path = get_abs_path(src_file_path)
    dst_dir_path = get_abs_path(dst_dir_path)
    if not os.path.exists(dst_dir_path):
        os.makedirs(dst_dir_path)

    dst_file_path = os.path.join(dst_dir_path, src_file_name)
    if os.path.exists(dst_file_path):
        os.remove(dst_file_path)

    # dst_file_name = src_file_path.rsplit('/', 1)[1]
    dst_file_path = dst_dir_path + src_file_name
    shutil.move(src_file_path, dst_file_path)

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


def get_abs_path(relative_path):
    file_path = None
    try:
        path, file_name = relative_path.rsplit('/', 1)
        d = os.getcwd()
        parent_path = Path(d).parent
        folder_path = os.path.join(str(parent_path), path)
        file_path = os.path.join(folder_path, file_name)
    except Exception as e:
        print(e)
    return file_path

