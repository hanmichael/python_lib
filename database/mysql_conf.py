#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import sys_path

class MysqlConfig(object):
    '''
    mysql config

    @hostname: localhost
    @port: 3306
    @user: chenguolin
    @password: password
    @db: database name
    @charset: default utf-8

    '''
    def __init__(self, **kwargs):
        self.hostname = kwargs.get('hostname') or ''
        self.port = kwargs.get('port') or '0'
        self.user = kwargs.get('user') or ''
        self.password = kwargs.get('password') or ''
        self.db = kwargs.get('db') or ''
        self.charset = kwargs.get('charset') or 'utf8'


    def __debug_config__(self):
        print 'Mysql Config:'
        print 'hostname = %s' % self.hostname
        print 'port = %s' % self.port
        print 'user = %s' % self.user
        print 'password = %s' % self.password
        print 'db = %s' % self.db
        print 'charset = %s' % self.charset
        print ''
