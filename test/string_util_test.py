#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append('../py_util')
import string_util

class StringUtilTest(unittest.TestCase):
    def test_is_string(self):
        obj = 1
        self.assertFalse(string_util.is_string(obj))

        obj = u'中国'
        self.assertTrue(string_util.is_string(obj))

        obj = 'github'
        self.assertTrue(string_util.is_string(obj))

if __name__ == '__main__':
    unittest.main()
