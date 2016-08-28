#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import unittest
sys.path.append('../py_util')
import json_util

class JsonUtilTest(unittest.TestCase):
    def test_json_2_str(self):
        json_obj = {'key':'value'}
        str_obj = json_util.json_2_str(json_obj)
        print str_obj

        json_obj = {'key':'value', '标题':'中国'}
        str_obj = json_util.json_2_str(json_obj)
        print str_obj

    def test_str_2_json(self):
        str_obj = '{"key":"value"}'
        json_obj = json_util.str_2_json(str_obj)
        print json_obj

        str_obj = '{"key":"value", "标题":"中国"}'
        json_obj = json_util.str_2_json(str_obj)
        print json_obj

if __name__ == '__main__':
    unittest.main()
