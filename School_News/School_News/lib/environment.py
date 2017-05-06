# -*- coding: utf-8 -*-
import os


def mkdir(path):
    path_list = os.path.abspath(path).split(os.sep)
    r_path = '{}{}'.format(path_list.pop(0), os.sep)
    while path_list:
        r_path = os.path.join(r_path, path_list.pop(0))
        if not os.path.exists(r_path):
            os.mkdir(r_path)
    return path


class Environment:
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    result_path = mkdir(os.path.join(root_path, 'result'))
    config_path = mkdir(os.path.join(root_path, 'config'))
    modified_file = os.path.join(result_path, 'modified.json')


env = Environment
