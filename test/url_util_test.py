#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append('../py_util')
import url_util

class UrlUtilTest(unittest.TestCase):
    def test_url_quote(self):
        url = "http://www.xxx.com/?q= github&page=1"
        quote_url = url_util.url_quote(url)
        self.assertEqual('http%3A//www.xxx.com/%3Fq%3D%20github%26page%3D1', quote_url)

    def test_url_unquote(self):
        url = "http://www.xxx.com/?q= github&page=1"
        quote_url = url_util.url_quote(url)
        self.assertEqual(url, url_util.url_unquote(quote_url))

    def test_url_md5(self):
        url = "http://www.xxx.com/?q= github&page=1"
        self.assertEqual('4bc2fd7697acde9086b22e201cc27875', url_util.url_md5(url))

    def test_url_signature(self):
        url = "http://www.xxx.com/?q= github&page=1"
        self.assertEqual('4bc2fd76-97acde90-86b22e20-1cc27875', url_util.url_signature(url))

    def test_url_encode(self):
        url = "http://www.xxx.com/?q= github&page=1"
        self.assertEqual('aHR0cDovL3d3dy54eHguY29tLz9xPSBnaXRodWImcGFnZT0x', url_util.url_encode(url))

    def test_url_decode(self):
        url = "http://www.xxx.com/?q= github&page=1"
        encode_url = url_util.url_encode(url)
        self.assertEqual(url, url_util.url_decode(encode_url))

if __name__ == '__main__':
    unittest.main()
