## 1. 说明
python 基础库, 封装了大部分常用的操作, 提供API直接调用
安装脚本setup.py对Linux和Mac系统做了兼容

## 2. setup
```
setup_status = setup(
    name = "python_lib",
    version = "2.0",
    packages = find_packages(),
    install_requires = [
        'Requests >= 2.10.1',
        'tldextract >= 2.0.1',
        'MySQL-python >= 1.2.5'
    ],
    author = "chenguolin",
    author_email = "cgl1079743846@gmail.com",
    description = "This is an about python lib package"
)
```

## 3. 安装使用方法
1. python setup.py install
   默认会把python_lib这个egg包安装到python的dist-packages目录下
2. from python_lib.common import simhash
   从python_lib的common库引入simhash

## 4. 基础库
### 4.1 jieba
1. jieba

### 4.2 python_lib
1. common
2. database
3. fslib
4. hadoop
5. log
6. processor
7. spark
8. word_segment

## 5. 常见问题
### 5.1 Ubuntu
```
1. "ImportError: No module named setuptools"
   解决方法: sudo apt-get install python-setuptools
2. "EnvironmentError: mysql_config not found"
   解决方法: sudo apt-get install libmysqlclient-dev
3. "error: command 'gcc' failed with exit status 1"
   解决方法: sudo apt-get install python-dev
4. 安装 jieba pkg的时候会出现tar包下载失败问题，所以并未把jieba的依赖写在setup里面，而是单独在setup脚本内写一个函数使用安装
```
### 5.2 Mac 
```
1. 首先先安装brew
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"  
2. "EnvironmentError: mysql_config not found"
   解决方法: brew isntall mysql
```
