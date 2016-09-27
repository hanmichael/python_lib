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
        'MySQL-python >= 1.2.5',
        'selenium >= 2.0.0'
    ],
    author = "chenguolin",
    author_email = "cgl1079743846@gmail.com",
    description = "This is an about Python util package"
)
##############################################################################################################
def install_phantomjs():
    if os.path.exists('/bin/phantomjs'):
        return
    status, output = commands.getstatusoutput('uname -m')
    phantomjs_pkg_url = 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-i686.tar.bz2'
    if output.find('64') > 0:
        phantomjs_pkg_url = 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2'
    try:
        os.system('wget %s -O phantomjs.tar.bz2' % phantomjs_pkg_url)
        os.system('tar -jxvf phantomjs.tar.bz2')
        os.system('sudo cp ./phantomjs-2.1.1*/bin/phantomjs /bin/')
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
        os.system('cd ./jieba && sudo python setup.py install')
        os.system('rm -rf jieba*')
install_jieba()
##############################################################################################################
def check_install_status():
    install_status = False
    install_path = ''
    if "install" in sys.argv:
        lib_paths = [get_python_lib()]
        if lib_paths[0].startswith("/usr/lib/"):
            # We have to try also with an explicit prefix of /usr/local in order to
            # catch Debian's custom user site-packages directory.
            lib_paths.append(get_python_lib(prefix="/usr/local"))
        for lib_path in lib_paths:
            existing_path = os.path.abspath(os.path.join(lib_path, "python_util-0.1-py2.7.egg"))
            if os.path.exists(existing_path):
                install_path = existing_path
                install_status = True
                break
    if install_status is True:
        sys.stdout.write('''
            ==========================================
            Success to install python_util, path:[%s]'
            ==========================================
        ''' % install_path)
    else:
        sys.stderr.write('''
            ==========================================
            Fail to install python_util'
            ==========================================
        ''')
check_install_status()
##############################################################################################################
try:
    os.system('rm -rf dist')
    os.system('rm -rf build')
    os.system('rm -rf python_util.egg-info')
except Exception,e:
    print "clean install info exception:[%s]" % str(e)
