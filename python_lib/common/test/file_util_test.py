#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append('../py_util')
import file_util

class FileUtilTest(unittest.TestCase):
    @unittest.skip("skip exists function")
    def test_exists(self):
        self.assertTrue(file_util.exists('/tmp/file_util/'))
        self.assertFalse(file_util.exists('/tmp/file_util2/'))
        self.assertTrue(file_util.exists('/tmp/file_util/file.dat'))
        self.assertFalse(file_util.exists('/tmp/file_util2/file2.dat'))

    @unittest.skip("skip make_dir function")
    def test_make_dir(self):
        self.assertTrue(file_util.make_dir('/tmp/file_util/'))
        self.assertTrue(file_util.make_dir('/tmp/file_util_tmp/'))

    @unittest.skip("skip remove_dir function")
    def test_remove_dir(self):
        self.assertTrue(file_util.remove_dir('/tmp/file_util_tmp/'))
        self.assertTrue(file_util.remove_dir('/tmp/file_util/'))

    @unittest.skip("skip touch_file function")
    def test_touch_file(self):
        self.assertTrue(file_util.make_dir('/tmp/file_util/'))
        self.assertTrue(file_util.touch_file('/tmp/file_util/file.dat'))
        self.assertTrue(file_util.exists('/tmp/file_util/file.dat'))
        self.assertFalse(file_util.touch_file('/tmp/file_util/file.dat'))
        self.assertTrue(file_util.touch_file('/tmp/file_util/file.dat', ignore_exist=True))

    @unittest.skip("skip remove_file function")
    def test_remove_file(self):
        self.assertTrue(file_util.remove_file('/tmp/file_util/file.dat'))
        self.assertTrue(file_util.remove_file('/tmp/file_util/file.dat'))

    @unittest.skip("skip list_dir function")
    def test_list_dir(self):
        print file_util.list_dir('/tmp/file_util/')
        print file_util.list_dir('/tmp/file_util/', filter_file=True)
        print file_util.list_dir('/tmp/file_util/', filter_dir=True)

    @unittest.skip("skip read_file function")
    def test_read_file(self):
        print file_util.read_file('/tmp/file_util/file.dat')

    @unittest.skip("skip write_file function")
    def test_write_file(self):
        content = 'test write file\n'
        self.assertTrue(file_util.write_file('/tmp/file_util/file.dat', content))
        print file_util.read_file('/tmp/file_util/file.dat')
        self.assertTrue(file_util.write_file('/tmp/file_util/file.dat', content, append=True))
        print file_util.read_file('/tmp/file_util/file.dat')

    @unittest.skip("skip read_file_lines function")
    def test_read_file_lines(self):
        print file_util.read_file_lines('/tmp/file_util/file.dat')

if __name__ == '__main__':
    unittest.main()
