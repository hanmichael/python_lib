#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append('../py_util')
import url_util

class UrlUtilTest(unittest.TestCase):
    def test_url_valid(self):
        self.assertFalse(url_util.url_valid(''))
        self.assertFalse(url_util.url_valid('xdfsdfd'))
        self.assertTrue(url_util.url_valid('http://www.baidu.com/?q=iphone6'))
        self.assertTrue(url_util.url_valid('ftp://www.baidu.com/?q=iphone6'))
        self.assertTrue(url_util.url_valid('https://www.baidu.com/?q=iphone6'))
        self.assertTrue(url_util.url_valid('http://127.0.0.1:9090/?q=iphone6&key=page1'))
        self.assertTrue(url_util.url_valid('http://localhost:9090/?q=iphone6&key=page1'))
        self.assertTrue(url_util.url_valid('www.baidu.com'))
        self.assertTrue(url_util.url_valid('baidu.com'))

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

    def test_get_host(self):
        self.assertEqual(None, url_util.get_host(''))
        self.assertEqual(None, url_util.get_host('sfdsfdsf'))
        self.assertEqual("www.baidu.com", url_util.get_host('http://www.baidu.com/?q=iphone6'))
        self.assertEqual("www.baidu.com", url_util.get_host('ftp://www.baidu.com/?q=iphone6'))
        self.assertEqual("www.baidu.com", url_util.get_host('https://www.baidu.com/?q=iphone6'))
        self.assertEqual("127.0.0.1", url_util.get_host('http://127.0.0.1:9090/?q=iphone6&key=page1'))
        self.assertEqual("localhost", url_util.get_host('http://localhost:9090/?q=iphone6&key=page1'))
        self.assertEqual("www.baidu.com", url_util.get_host('www.baidu.com'))

    def test_get_domain(self):
        self.assertEqual(None, url_util.get_domain(''))
        self.assertEqual(None, url_util.get_domain('sfdsfdsf'))
        self.assertEqual("baidu.com", url_util.get_domain('http://www.baidu.com/?q=iphone6'))
        self.assertEqual("baidu.com", url_util.get_domain('ftp://www.baidu.com/?q=iphone6'))
        self.assertEqual("baidu.com", url_util.get_domain('https://www.baidu.com/?q=iphone6'))
        self.assertEqual("127.0.0.1", url_util.get_domain('http://127.0.0.1:9090/?q=iphone6&key=page1'))
        self.assertEqual("localhost", url_util.get_domain('http://localhost:9090/?q=iphone6&key=page1'))
        self.assertEqual("baidu.com", url_util.get_domain('www.baidu.com'))
        self.assertEqual("baidu.com", url_util.get_domain('baidu.com'))
        self.assertEqual("cnn.com", url_util.get_domain('http://forums.news.cnn.com/'))
        self.assertEqual("bbc.co.uk", url_util.get_domain('forums.bbc.co.uk'))

if __name__ == '__main__':
    unittest.main()
