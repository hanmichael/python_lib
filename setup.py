#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import commands
from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib

setup_status = setup(
    name = "python_util",
    version = "1.0",
    packages = find_packages(),
    package_data = {
        '': ['*.py']
    },
    install_requires = [
        'Requests >= 2.10.1',
        'tldextract >= 2.0.1',
        'MySQL-python >= 1.2.5'
    ],
    author = "chenguolin",
    author_email = "cgl1079743846@gmail.com",
    description = "This is an about Python util package"
)

# check platform
import platform
platform_system = platform.system()
##############################################################################################################
def install_phantomjs():
    phantomjs_bin = '/bin/phantomjs'
    if platform_system == 'Darwin':
        phantomjs_bin = '/usr/local/bin/phantomjs'
    if os.path.exists(phantomjs_bin):
        return
    status, output = commands.getstatusoutput('uname -m')
    phantomjs_pkg_url = 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-i686.tar.bz2'
    if output.find('64') > 0:
        phantomjs_pkg_url = 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2'
    try:
        os.system('wget %s -O phantomjs.tar.bz2' % phantomjs_pkg_url)
        os.system('tar -jxvf phantomjs.tar.bz2')
        os.system('mv phantomjs-* phantomjs')
        if platform_system == 'Darwin':
            os.system('cp ./phantomjs/bin/phantomjs /usr/local/bin/')
            os.system('chmod 755 /usr/local/bin/phantomjs')
        else:
            os.system('sudo cp ./phantomjs/bin/phantomjs /bin/')
            os.system('sudo chmod 755 /bin/phantomjs')
        os.system('rm -rf ./phantomjs*')
    except Exception,e:
        print "install PhantomJs exception:[%s]" % str(e)
install_phantomjs()
##############################################################################################################
def install_jieba():
    try:
        import jieba
    except Exception,e:
        pkg_url = 'https://pypi.python.org/packages/f6/86/9e721cc52075a07b7d07eb12bcb5dde771d35332a3dae1e14ae4290a197a/jieba-0.38.zip#md5=c4b5f25631218caec249837870ed067a'
        os.system('wget %s -O jieba.zip' % pkg_url)
        os.system('unzip jieba.zip')
        os.system('mv jieba-* jieba')
        os.system('cd ./jieba && sudo python setup.py install && cd ..')
        os.system('rm -rf jieba*')
install_jieba()
##############################################################################################################
def install_selenium():
    try:
        import selenium
    except Exception,e:
        pkg_url = 'https://pypi.python.org/packages/3a/a3/e4ab60a0229a85f468a36367bc0672a4bca2720f24391eda33704a5f0ad5/selenium-3.0.1.tar.gz#md5=ed5da4a35e1e643a53386d3e8f5960af'
        os.system('wget %s -O selenium.tar.gz' % pkg_url)
        os.system('tar -xvzf selenium.tar.gz')
        os.system('mv selenium-* selenium')
        os.system('cd ./selenium && sudo python setup.py install && cd ..')
        os.system('rm -rf selenium*')
install_selenium()
##############################################################################################################
try:
    os.system('rm -rf dist')
    os.system('rm -rf build')
    os.system('rm -rf *.egg-info')
except Exception,e:
    print "clean install info exception:[%s]" % str(e)
