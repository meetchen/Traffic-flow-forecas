# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 14:47
# @Author  : 奥利波德
# @FileName: web.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
# coding:utf-8


import json

from urllib import parse

from wsgiref.simple_server import make_server


# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。

def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code

    start_response('200 OK', [('Content-Type', 'text/html')])

    # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get

    # 获取当前get请求的所有数据，返回是string类型

    params = parse.parse_qs(environ['QUERY_STRING'])

    # 获取get中key为name的值

    name = params.get('hour', [''])[0]




    return [json.dumps(dic).encode('utf-8')]


if __name__ == "__main__":
    port = 5088

    httpd = make_server("0.0.0.0", port, application)

    print("serving http on port {0}...".format(str(port)))

    httpd.serve_forever()
