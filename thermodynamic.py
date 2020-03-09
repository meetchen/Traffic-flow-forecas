# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 15:55
# @Author  : 奥利波德
# @FileName: thermodynamic.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
import pandas as pd


class ThermodynamicChart:
    data = pd.read_csv("latAndLon.csv")
    wd = pd.read_csv("./data/服创大赛-基站经纬度数据.csv")
    data['timestamp'] = data['timestamp'].apply(lambda x: x // 10000)

    def __init__(self):
        data = pd.read_csv("latAndLon.csv")
        wd = pd.read_csv("./data/服创大赛-基站经纬度数据.csv")

    def getJson(self, data, wd=wd):
        h = data.groupby('laci').count().reset_index(drop=False)
        h = pd.merge(h, wd, on="laci")
        h = h[['timestamp', 'longitude_y', 'latitude_y']]
        h = h.rename(columns={'timestamp': 'count', 'longitude_y': 'lng', 'latitude_y': 'lat'})
        result = h.to_json(orient='records')
        return result

    def getGroupByHour(self, data=data, hour=0):
        data = data.groupby(by='timestamp').get_group(2018100300 + hour)
        return data

