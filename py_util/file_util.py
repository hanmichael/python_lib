#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil

def exists(dir_path):
    """
    Check file/dir exist

    @dir_path: file or dir path, don't care

    return True/False
    """
    if os.path.exists(dir_path):
        return True
    else:
        return False

def make_dir(dir_path, mode=0777):
    """
    Create dir

    @dir_path: dir path
    @mode: dir mode, defaulte 0777

    return True/False
    """
    if exists(dir_path):
        return False
    try:
        os.mkdir(dir_path, mode)
        return True
    except Exception, e:
        sys.stderr.write('make dir:[%s] exception:[%s]' % (dir_path, str(e)))
        return False

def remove_dir(dir_path):
    """
    Remove dir, don't care is empty dir

    @dir_path: dir path

    return True/False
    """
    if exists(dir_path) is False:
        return True
    try:
        shutil.rmtree(dir_path)
        return True
    except Exception, e:
        sys.stderr.write('remove dir:[%s] exception:[%s]' % (dir_path, str(e)))
        return False

def touch_file(file_path, ignore_exist = False):
    """
    Touch file

    @file_path: file path
    @ignore_exist: judge ignore exist file

    return True/False
    """
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
    """
    Remove file

    @file_path: file path

    return True/False
    """
    if exists(file_path) is False:
        return True
    try:
        os.remove(file_path)
        return True
    except Exception, e:
        sys.stderr.write('remove file:[%s] exception:[%s]' % (file_path, str(e)))
        return False

def list_dir(dir_path, filter_file = False, filter_dir = False):
    """
    List dir

    @dir_path: dir path
    @filter_file: is to filter normal file
    @filter_dir: is to filter dir

    return list
    """
    if exists(dir_path) is False:
        return []
    try:
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
    except Exception, e:
        sys.stderr.write('list dir:[%s] exception:[%s]' % (dir_path, str(e)))
        return []
