#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append('../py_util')
import shell_util

class ShellUtilTest(unittest.TestCase):
    def test_run_cmd(self):
        cmd = 'ls -lsrt'
        cmd_status = shell_util.run_cmd(cmd)
        print cmd_status.status
        print cmd_status.output
        print "=============================="

        cmd = 'ls -ls5t'
        cmd_status = shell_util.run_cmd(cmd)
        print cmd_status.status
        print cmd_status.output
        print "=============================="

if __name__ == '__main__':
    unittest.main()
