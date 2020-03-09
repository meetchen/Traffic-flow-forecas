# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 9:39
# @Author  : 奥利波德
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507

import pandas as pd


def getJson(data, wd):
    h = data.groupby('laci').count().reset_index(drop=False)
    h = pd.merge(h, wd, on="laci")
    h = h[['timestamp', 'longitude_y', 'latitude_y']]
    h = h.rename(columns={'timestamp': 'count', 'longitude_y': 'lng', 'latitude_y': 'lat'})
    result = h.to_json(orient='records')
    return result


def getGroupByHour(data, hour):
    print(type(hour))
    print(hour)
    data['timestamp'] = data['timestamp'].apply(lambda x: x // 10000)
    data = data.groupby(by='timestamp').get_group(2018100300 + hour)
    return data


data = pd.read_csv("latAndLon.csv")
data = getGroupByHour(data, 5)
# data = pd.read_csv("4.csv")
wd = pd.read_csv("E:\Python_workspace\Traffic-flow-forecas\data\服创大赛-基站经纬度数据.csv")
result = getJson(data, wd)
print(result)
