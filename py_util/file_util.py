#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

'''
don't care dir_path it's a file or a directory
'''
def dir_exist(dir_path):
    if os.path.exists(dir_path):
        return True
    else:
        return False

def make_dir(dir_path, mode=0777):
    if dir_exist(dir_path):
        return False
    try:
        os.makdir(dir_path, mode)
        return True
    except OSError, e:
        sys.stderr.write('make dir exception:[%s]' % str(e))
        return False
