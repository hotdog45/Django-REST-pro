# -*- coding: utf-8 -*-
#  SXShop  ---  2018/4/24  ---  PyCharm
import multiprocessing

bind = "127.0.0.1:8080"
workers = 2  #workers是工作线程数，一般设置成：服务器CPU个数 + 1
# errorlog = '/EdmureBlog/gunicorn.error.log'
#accesslog = './gunicorn.access.log'
#loglevel = 'debug'
proc_name = 'SXShop'


