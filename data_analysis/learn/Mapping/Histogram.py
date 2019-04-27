#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 10:06
# @Author  : zengsk in HoHai
# @File    : Histogram.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Titanic = pd.read_csv(r'F:\python\data_analysis\learn\Mapping\data\titanic_train.csv');
# 缺失值处理
any(Titanic.Age.isnull());
Titanic.dropna(subset=['Age'], inplace=True);
# 绘制直方图
plt.rcParams['font.sans-serif'] = ['SimHei'];
plt.rcParams['axes.unicode_minus'] = False;
plt.hist(x = Titanic.Age, # 指定绘图数据
         bins = 20, # 指定直方图图块个数
         color= 'steelblue',
         edgecolor = 'black',
         );
plt.xlabel('年龄');
plt.ylabel('频数');
plt.title('乘客年龄分布');
plt.show();
