#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append('../py_util')
import config_parse
import json_util

class ConfigParseTest(unittest.TestCase):
    def test_config_parse(self):
        config_file = ''
        config_dict = config_parse.config_parse(config_file)
        print config_dict

        config_file = './data/config.dat'
        config_dict = config_parse.config_parse(config_file)
        print config_dict

        config_file = './data/config.dat'
        config_dict = config_parse.config_parse(config_file)
        print json_util.json_2_str(config_dict, readable=True)

if __name__ == '__main__':
    unittest.main()
