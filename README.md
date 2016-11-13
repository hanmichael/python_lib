## 1. 说明
python 基础库, 封装了大部分常用的操作, 提供API直接调用
安装脚本setup.py对Linux和Mac系统做了兼容

## 2. 使用方法
1. python setup.py install
2. form py_util import file_util
3. test: 单元测试

## 3. 依赖
1. version: python2.7
2. linux: ubuntu 12.04
3. requires pkg: 
   1. Requests >= 2.10.1
   2. tldextract >= 2.0.1
   3. selenium >= 2.0.0
   4. PhantomJs >= 2.1.1
   5. jieba >= 0.1
4. 依赖的第三方库在install的时候会自动安装，用户无需自己安装
5. 注意: selenium,PhantomJs,jieba通过setuptools无法自动安装, 通过Python代码手动下载实现安装

## 4. 基础库
1. datetime_util: 日期和时间相关api
2. file_util: 文件操作相关api
3. url_util: url操作相关api
4. request_util: http request操作api
5. string_util: string 基础api
6. shell_util: linux shell操作api
7. mysql_util: mysql操作api
8. json_util: json api
9. crawl_util: crawl page util api  //Mac os下使用Phantomjs的API可能会无法使用
10. config_parse: parse config file
11. word_segment: word segment tool
12. simhash: python calc simhash api

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
