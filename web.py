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
from thermodynamic import ThermodynamicChart


def getHour(environ):
    params = parse.parse_qs(environ['QUERY_STRING'])
    hour = params.get('hour', [''])[0]
    ther = ThermodynamicChart()
    data = ther.getGroupByHour(hour=int(hour))
    data = ther.getJson(data)
    return data


def getAll(environ):
    result = "["
    ther = ThermodynamicChart()
    for i in range(0, 24):
        data = ther.getGroupByHour(hour=i)
        data = ther.getJson(data)
        result = result+(str(data)+",")
    return result[:-1]+"]"


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json;charset=UTF-8')])
    position = environ['PATH_INFO']
    function = None
    for url in urls:
        if url[0] == position:
            function = url[1]
            break
    if function:
        info = function(environ)
    else:
        info = 'Wa oh 404'

    return [info.encode('utf-8')]


if __name__ == "__main__":
    urls = [
        ('/getHour', getHour),
        ('/getAll', getAll),
    ]
    port = 1724
    httpd = make_server("0.0.0.0", port, application)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()
