#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 20:25
# @Author  : zengsk in HoHai
# @File    : bar_plot.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

################ 单个离散变量的条形图 ######################

GDP = pd.read_excel(r'F:\python\data_analysis\learn\Mapping\data\Province GDP 2017.xlsx');
plt.style.use('ggplot'); # 设置绘图风格
plt.rcParams['font.sans-serif'] = ['SimHei'];
plt.bar(left = range(GDP.shape[0]),
        height = GDP.GDP,
        tick_label = GDP.Province,  #指定条形图的刻度标签
        width = 0.5,
        edgecolor = 'black',
        color = 'steelblue');
plt.xlabel('省份');
plt.ylabel('GDP(万亿)');
plt.title("2017年度各个省份GDP分布");
# 为每个条形图添加数值标签
for x, y in enumerate(GDP.GDP):
    plt.text(x, y+0.1, '%s' % round(y,1), ha='center');
# 显示
plt.show();

################ 堆叠条形图 ################
Industry_GDP = pd.read_excel(r'F:\python\data_analysis\learn\Mapping\data\Industry_GDP.xlsx');
# 取出不同季度标签 作为x轴刻度
Quarters = Industry_GDP.Quarter.unique();
#取数据
Ind1 = Industry_GDP.GDP[Industry_GDP.Industry_Type == '第一产业'];
Ind1.index = range(len(Quarters));
Ind2 = Industry_GDP.GDP[Industry_GDP.Industry_Type == '第二产业'];
Ind2.index = range(len(Quarters));
Ind3 = Industry_GDP.GDP[Industry_GDP.Industry_Type == '第三产业'];
# 各季度下第一产业
plt.bar(left = range(len(Quarters)), height = Ind1,
        color = 'steelblue', edgecolor = 'black', width = 0.5,
        label = '第一产业', tick_label = Quarters);
# 各季度下第二产业
plt.bar(left = range(len(Quarters)), height = Ind2, bottom = Ind1,
        color = 'green', edgecolor = 'black', width = 0.5,
        label = '第二产业');
# 各季度下第三产业
plt.bar(left = range(len(Quarters)), height = Ind3, bottom = Ind1+Ind2,
        color = 'red', edgecolor = 'black', width = 0.5,
        label = '第三产业');

plt.xlabel('季度');
plt.ylabel('生产总值(亿)');
plt.title('2017各季度三个产业总值');
plt.legend();
plt.show();

################# 多变量交错条形图 ####################

# 读入数据
HuRun = pd.read_excel(r'C:\Users\Administrator\Desktop\HuRun.xlsx')
# 取出城市名称
Cities = HuRun.City.unique()
# 取出2016年各城市亿万资产家庭数
Counts2016 = HuRun.Counts[HuRun.Year == 2016]
# 取出2017年各城市亿万资产家庭数
Counts2017 = HuRun.Counts[HuRun.Year == 2017]

# 绘制水平交错条形图
bar_width = 0.4
plt.bar(left = np.arange(len(Cities)), height = Counts2016, label = '2016', color = 'steelblue', width = bar_width)
plt.bar(left = np.arange(len(Cities))+bar_width, height = Counts2017, label = '2017', color = 'indianred', width = bar_width)
# 添加刻度标签（向右偏移0.225）
plt.xticks(np.arange(5)+0.2, Cities)
# 添加y轴标签
plt.ylabel('亿万资产家庭数')
# 添加图形标题
plt.title('近两年5个城市亿万资产家庭数比较')
# 添加图例
plt.legend()
# 显示图形
plt.show()




