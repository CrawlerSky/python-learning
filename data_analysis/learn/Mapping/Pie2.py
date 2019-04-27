#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 20:07
# @Author  : zengsk in HoHai
# @File    : Pie2.py

import pandas as pd
import matplotlib.pyplot as plt

# 构造序列
data = pd.Series({'南京':0.2515, '上海':0.3721, '杭州':0.3336, '成都':0.0368, '广州':0.0057});
data.name = '';
plt.rcParams['font.sans-serif'] = ['SimHei'];
plt.rcParams['axes.unicode_minus'] = False;
plt.axes(aspect = 'equal');

data.plot(kind = 'pie',
          autopct = '%.2f%%',
          radius = 1,
          startangle = 180,
          title = '城市xxx水平分布',
          wedgeprops = {'linewidth': 1.5, 'edgecolor': 'green'},
          textprops = {'fontsize': 10, 'color': 'black'}
          );
plt.show();


