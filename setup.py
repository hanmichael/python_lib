import os
import sys
from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib

setup_status = setup(
    name = "python_util",
    version = "0.1",
    packages = find_packages(),
    package_data = {
        '': ['*.py']
    },
    author = "chenguolin",
    author_email = "cgl1079743846@gmail.com",
    description = "This is an about Python util package"
)

install_status = False
install_path = ''
if "install_egg_info" in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):
        # We have to try also with an explicit prefix of /usr/local in order to
        # catch Debian's custom user site-packages directory.
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "python_util-0.1.egg-info"))
        if os.path.exists(existing_path):
            install_path = existing_path
            install_status = True
            break

if install_status is True:
    sys.stdout.write('''
===========================================================
Success to install python_util, path:[%s]'
===========================================================\n
''' % install_path)
else:
    sys.stderr.write('''
 ===========================================================
 Fail to install python_util'
 ===========================================================\n
 ''')
