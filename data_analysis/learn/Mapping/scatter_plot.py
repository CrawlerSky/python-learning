#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 16:56
# @Author  : zengsk in HoHai
# @File    : scatter_plot.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv(r'F:\python\data_analysis\learn\Mapping\data\iris.csv')

plt.rcParams['font.sans-serif'] = ['SimHei'];
plt.rcParams['axes.unicode_minus'] = False;

# 绘图
plt.scatter(x = iris.Petal_Width,
            y = iris.Petal_Length,
            color = 'steelblue'
            )
plt.xlabel('花瓣宽度')
plt.ylabel('花瓣长度')
plt.title('鸢尾花花瓣的长度与宽度的关系')
plt.show()