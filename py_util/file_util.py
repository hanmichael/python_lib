#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
import shutil
import warnings
#warnings.filterwarnings('ignore')

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('file_util')

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
        logger.warning('dir:[%s] has exist' % dir_path)
        return True
    try:
        os.mkdir(dir_path, mode)
        return True
    except Exception, e:
        logger.error('make dir:[%s] exception:[%s]' % (dir_path, str(e)))
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
        logger.error('remove dir:[%s] exception:[%s]' % (dir_path, str(e)))
        return False

def touch_file(file_path, ignore_exist = False):
    """
    Touch file

    @file_path: file path
    @ignore_exist: judge ignore exist file

    return True/False
    """
    if exists(file_path) and ignore_exist is False:
        logger.error('file has exist touch fail [%s]' % file_path)
        return False
    try:
        fh = open(file_path, 'w')
        fh.close()
        return True
    except Exception, e:
        logger.error('touch file:[%s] exception:[%s]' % (file_path, str(e)))
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
        logger.error('remove file:[%s] exception:[%s]' % (file_path, str(e)))
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
        logger.error('list dir:[%s] exception:[%s]' % (dir_path, str(e)))
        return []

def read_file(file_path):
    """
    Read file

    @file_path: file path

    return content
    """
    try:
        mode = 'r'
        fh = open(file_path, mode)
        content = fh.read()
        fh.close()
        return content
    except Exception, e:
        logger.error('read file:[%s] exception:[%s]' % (file_path, str(e)))
        return None

def write_file(file_path, content, append=False):
    """
    Write content to file

    @file_path: file path
    @content: write content
    @append: True express append content to file

    return True/False
    """
    try:
        mode = 'w'
        if append: mode = 'a'
        fh = open(file_path, mode)
        fh.write(content)
        fh.close()
        return True
    except Exception, e:
        logger.error('write file:[%s] exception:[%s]' % (file_path, str(e)))
        return False

def read_file_lines(file_path):
    """
    Read file

    @file_path: file path

    return content
    """
    try:
        mode = 'r'
        fh = open(file_path, mode)
        lines = fh.readlines()
        fh.close()
        return lines
    except Exception, e:
        logger.error('read file:[%s] lines exception:[%s]' % (file_path, str(e)))
        return []
