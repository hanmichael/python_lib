#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
import warnings
import commands

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('shell_util')
logger.setLevel(logging.INFO)

class CmdStatus(object):
    def __init__(self, status=-1, output=''):
        self.status = status
        self.output = output

def run_cmd(cmd):
    """
    Python run shell cmd

    @cmd: string command

    return CmdStatus obj
    """

    try:
        cmd_status = CmdStatus()
        try:
            res_tuple = commands.getstatusoutput(cmd)
        except Exception,e:
            res_tuple = None
        if res_tuple is None or len(res_tuple) != 2:
            logger.error('run command:[%s] get invalid result' % cmd)
            return cmd_status
        cmd_status.status = res_tuple[0]
        cmd_status.output = res_tuple[1]
        return cmd_status
    except Exception,e:
        logger.error('run command:[%s] exception:[%s]' % (cmd, str(e)))
        return None
