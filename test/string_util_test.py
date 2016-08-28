#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
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

    def test_is_url(self):
        url = 'url'
        self.assertFalse(string_util.is_url(url))

        url = 'http://www.baidu.com/?q=query&key=value'
        self.assertTrue(string_util.is_url(url))

        url = 'http://www.baidu.com/?q=query&key=value'
        self.assertFalse(string_util.is_url(url, ['https']))

    def test_is_email(self):
        email = 'email'
        self.assertFalse(string_util.is_email(email))

        email = 'cgl10xxxxxx46@gmail.com'
        self.assertTrue(string_util.is_email(email))

    def test_is_json(self):
        json_str = '{"key"}'
        self.assertFalse(string_util.is_json(json_str))

        json_str = '{"key": "value"}'
        self.assertTrue(string_util.is_json(json_str))

        json_str = '{"标题": "中国"}'
        self.assertTrue(string_util.is_json(json_str))

    def test_is_ip(self):
        ip_str = '127'
        self.assertFalse(string_util.is_ip(ip_str))

        ip_str = '127.0'
        self.assertFalse(string_util.is_ip(ip_str))

        ip_str = '127.0.0'
        self.assertFalse(string_util.is_ip(ip_str))

        ip_str = '127.0.0.1'
        self.assertTrue(string_util.is_ip(ip_str))

if __name__ == '__main__':
    unittest.main()
