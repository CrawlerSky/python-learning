#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 17:08
# @Author  : zengsk in HoHai
# @File    : combine_plot.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#################### 多个图形合并绘制在一个图片上 #################

# 读取数据
Prod_Trade = pd.read_excel(r'F:\python\data_analysis\learn\Mapping\data\Prod_Trade.xlsx')

Prod_Trade['year'] = Prod_Trade.Date.dt.year # 获取交易年份
Prod_Trade['month'] = Prod_Trade.Date.dt.month # 获取交易月份

# 绘图
plt.rcParams['font.sans-serif'] = ['SimHei'];
plt.rcParams['axes.unicode_minus'] = False;
# 设置大图框的长和宽
plt.figure(figsize=(12,6))

######### 第一个子图
subplot1 = plt.subplot2grid(shape=(2,3),  loc=(0,0))

# 统计2012年个订单等级的数据量
Class_Counts = Prod_Trade.Order_Class[Prod_Trade.year == 2012].value_counts()
Class_Precent = Class_Counts/Class_Counts.sum()
# 绘制饼图
subplot1.set_aspect(aspect = 'equal')
subplot1.pie(x = Class_Precent.values,
        labels=Class_Precent.index,
        autopct='%.2f%%'
        )
subplot1.set_title('各等级订单比例')

######### 第二个子图
subplot2 = plt.subplot2grid(shape=(2,3), loc=(0,1))
# 统计2012年每月的销售额
Month_Sales = Prod_Trade[Prod_Trade.year == 2012].groupby(by = 'month').aggregate({'Sales':np.sum})

Month_Sales.plot(title = '2012年各月销售趋势', ax = subplot2, legend = False)
subplot2.set_xlabel('')

######### 第三个子图: 绘制各运输方式的成本箱体图
subplot3 = plt.subplot2grid(shape=(2,3), loc=(0,2), rowspan=2)
group_transport = Prod_Trade.groupby('Transport')
trans_cost = []
tansports = Prod_Trade.Transport.unique()
for trans in tansports:
    trans_cost.append(Prod_Trade.Trans_Cost[Prod_Trade.Transport == trans])
plt.boxplot(x = trans_cost,
            patch_artist=True,
            labels=tansports,
            showmeans=True,
            boxprops={'color':'black', 'facecolor':'steelblue'},
            flierprops={'marker':'o', 'markerfacecolor':'red', 'markersize':2},
            meanprops={'marker':'D','markerfacecolor':'Indianred','markersize':4},
            medianprops={'linestyle':'--', 'color':'orange'}
            );
plt.xlabel('Transports');
plt.ylabel('Trans-Cost');
plt.title('各运输方式成本分布');

# sns.boxplot(x='Transport', y='Trans_Cost', data='Prod_Trade', ax=subplot3)
# subplot3.set_title('各运输方式成本分布')
# subplot3.set_xlabel('')
# subplot3.set_ylabel('运输成本')


######## 第四个子图：绘制2012年客单价分布直方图
subplot4 = plt.subplot2grid(shape=(2,3), loc=(1,0), colspan=2)
plt.hist(x = Prod_Trade.Sales[Prod_Trade.year == 2012], # 指定绘图数据
         bins = 20, # 指定直方图图块个数
         normed=True,
         color= 'steelblue',
         edgecolor = 'black',
         );
plt.xlabel('销售额');
plt.ylabel('频率');
plt.subplots_adjust(hspace = 0.6, wspace = 0.3)
plt.title('2012年客单价分布图')


# 2012年各单价分布直方图
# sns.distplot(Prod_Trade.Sales[Prod_Trade.year == 2012], bins=40, norm_hist=True,
#              ax = subplot4, hist_kws={'color':'steelblue'}, kde_kws={'linestyle':'--', 'color':'red'}
#              )
# subplot4.set_title('2012年个单价分布图')
# subplot4.set_xlabel('销售额')
# # 调整子图之间的水平间距和高度间距
# plt.subplots_adjust(hspace = 0.6, wspace = 0.3)
plt.show()
