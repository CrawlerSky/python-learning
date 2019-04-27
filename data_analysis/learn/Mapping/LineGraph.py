#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 16:21
# @Author  : zengsk in HoHai
# @File    : LineGraph.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

################# 绘制2017年第四季度微信文章阅读人数折线图 ##################
# 读取数据
weChat = pd.read_excel(r'F:\python\data_analysis\learn\Mapping\data\wechat.xlsx')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘图
plt.plot(weChat.Date, weChat.Counts,
         linestyle = '-',
         linewidth = 2,
         color = 'steelblue',
         marker = 'o',
         markersize = 6,
         markeredgecolor = 'black',
         markerfacecolor = 'brown'
         )
plt.xlabel('日期')
plt.ylabel('人数')
plt.title('每天文章阅读人数趋势')
plt.show()

# 绘图2
import matplotlib as mpl
plt.plot(weChat.Date, weChat.Counts,
         linestyle = '-',
         color = 'steelblue',
         label = '阅读人数'
         )
plt.plot(weChat.Date, weChat.Times,
         linestyle = '--',
         color = 'indianred',
         label = '阅读人次'
         )
#获取图的坐标信息
axes = plt.gca()
# 设置日期显示格式
date_format = mpl.dates.DateFormatter("%m-%d")
axes.xaxis.set_major_formatter(date_format)
# 设置x轴显示多少各日期刻度
xlocator = mpl.ticker.LinearLocator(10)
# 设置x 轴的刻度间隔
xlocator = mpl.ticker.MultipleLocator(7)
axes.xaxis.set_major_locator(xlocator)

# 将x轴刻度标签倾斜表示
plt.xticks(rotation = 45)

plt.xlabel('Date')
plt.ylabel('Counts')
plt.title('微信文章每天阅读人数和人次趋势')
plt.legend()
plt.show()
