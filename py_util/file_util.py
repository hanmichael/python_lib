#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil

'''
don't care dir_path it's a file or a directory
'''
def exists(dir_path):
    if os.path.exists(dir_path):
        return True
    else:
        return False

def make_dir(dir_path, mode=0777):
    if exists(dir_path):
        return False
    try:
        os.mkdir(dir_path, mode)
        return True
    except Exception, e:
        sys.stderr.write('make dir:[%s] exception:[%s]' % (dir_path, str(e)))
        return False

def remove_dir(dir_path):
    if exists(dir_path) is False:
        return True
    try:
        shutil.rmtree(dir_path)
        return True
    except Exception, e:
        sys.stderr.write('remove dir:[%s] exception:[%s]' % (dir_path, str(e)))
        return False

def touch_file(file_path, ignore_exist = False):
    if exists(file_path) and ignore_exist is False:
        sys.stderr.write('file has exist touch fail [%s]' % file_path)
        return False
    try:
        fh = open(file_path, 'w')
        fh.write('')
        fh.close()
        return True
    except Exception, e:
        sys.stderr.write('touch file:[%s] exception:[%s]' % (file_path, str(e)))
        return False

def remove_file(file_path):
    if exists(file_path) is False:
        return True
    try:
        os.remove(file_path)
        return True
    except Exception, e:
        sys.stderr.write('remove file:[%s] exception:[%s]' % (file_path, str(e)))
        return False

def list_dir(dir_path, filter_file = False, filter_dir = False):
    if exists(dir_path) is False:
        return []
    dir_all_files = os.listdir(dir_path)
    result_list = []
    for sub_file in dir_all_files:
        if sub_file.startswith('.'):
            continue
        abs_sub_file = dir_path + '/' + sub_file
        if os.path.isfile(abs_sub_file) and not filter_file:
            result_list.append(sub_file)
        elif os.path.isdir(abs_sub_file) and not filter_dir:
            result_list.append(sub_file + '/')
    return result_list

