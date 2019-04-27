#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 10:40
# @Author  : zengsk in HoHai
# @File    : box_plot.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
Sec_Buildings = pd.read_excel(r'F:\python\data_analysis\learn\Mapping\data\sec_buildings.xlsx');

# 绘图
plt.rcParams['font.sans-serif'] = ['SimHei'];
plt.rcParams['axes.unicode_minus'] = False;

plt.boxplot(x = Sec_Buildings.price_unit, # 指定绘图数据
            patch_artist = True,  # 是否自定义填充箱体
            showmeans=True, # 是否显示均值
            boxprops={'color':'black', 'facecolor':'steelblue'}, # 箱体属性
            flierprops={'marker':'o', 'markerfacecolor':'red', 'markersize':3}, # 异常点属性
            medianprops={'linestyle':'--', 'color':'orange'}, # 中位数属性
            meanprops={'marker':'D', 'markerfacecolor':'indianred', 'markersize':4}, # 均值点属性
            labels=[''] # 删除x轴的刻度, 否则会显示刻度 1
            );
plt.title('二手房单价分布箱体图');
plt.show();


################# 分组箱线图绘制 ###################
# 二手房在各个行政区的评价单价
group_region = Sec_Buildings.groupby('region');
avg_price = group_region.aggregate({'price_unit':np.mean}).sort_values('price_unit', ascending=False);

# 将不同行政区的二手房存储到列表
region_price = [];
for region in avg_price.index:
    region_price.append(Sec_Buildings.price_unit[Sec_Buildings.region == region]);
# 绘图
plt.boxplot(x = region_price,
            patch_artist=True,
            labels=avg_price.index,
            showmeans=True,
            boxprops={'color':'black', 'facecolor':'steelblue'},
            flierprops={'marker':'o', 'markerfacecolor':'red', 'markersize':2},
            meanprops={'marker':'D','markerfacecolor':'Indianred','markersize':4},
            medianprops={'linestyle':'--', 'color':'orange'}
            );
plt.xlabel('行政区');
plt.ylabel('单价（元）');
plt.title('不同行政区的二手房单价');
plt.show()



