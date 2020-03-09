# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 9:40
# @Author  : 奥利波德
# @FileName: data_preprocessing.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507

import numpy as np
import pandas as pd
import time


def get_localtime(timeStamp):
    timeStamp = int(timeStamp / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y%m%d%H%M%S", timeArray)
    return int(otherStyleTime)


if __name__ == '__main__':
    data = pd.read_csv('E:\Python_workspace\Traffic-flow-forecas\data\服创大赛-原始数据.csv', usecols=[0, 1, 2, 3])
    data = data[data['imsi'].str.contains('\*')==False]
    # data = data[data['imsi'].str.contains('\^')==False]
    # data = data[data['imsi'].str.contains('#')==False]

    # data = data.dropna(subset=['imsi', 'lac_id', 'cell_id'])
    # data['timestamp'] = data['timestamp'].apply(get_localtime)
    # data[['lac_id', 'cell_id']] = data[['lac_id', 'cell_id']].astype(int)
    # data = data[(data['timestamp'] / 1000000).astype('int64') == 20181003]
    # data.to_csv("1.csv", index=None)

    data1 = pd.read_csv("1.csv")
    data1['laci'] = data1['lac_id'].astype(str) + '-' + data1['cell_id'].astype(str)
    # data1.to_csv("2.csv", index=None)
    data2 = pd.read_csv('E:\Python_workspace\Traffic-flow-forecas\data\服创大赛-基站经纬度数据.csv')
    data3 = pd.merge(data1, data2, on='laci')
    data3 = data3.dropna()
    # data3.to_csv("latAndLon.csv", index=None)

    data4 = data3.groupby(by='imsi').apply(lambda x: x.sort_values('timestamp', ascending=True)).reset_index(drop=True)
    data4.to_csv("4.csv", index=None)

