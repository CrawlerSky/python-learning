#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 18:50
# @Author  : zengsk in HoHai
# @File    : Pie.py

# 导入第三方模块
import matplotlib.pyplot as plt

# 测试数据
edu = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057];
labels = ['中专', '大专', '本科', '硕士', '其它'];
explode = [0, .1, 0, 0, 0];
colors = ['#9999ff', '#ff9999', '#7777aa', '#2442aa', '#dd5555'];

# 绘制饼图
plt.rcParams['font.sans-serif'] = ['SimHei']; # 中文处理
plt.rcParams['axes.unicode_minus'] = False;  # 正常显示负数
plt.axes(aspect='equal');  # 控制饼图为正圆
plt.pie(x=edu,  # 绘图数据
        explode=explode, #指定突出显示部分
        colors=colors,   #颜色分配
        labels=labels,  # 标签,图例
        autopct='%.2f%%',  # 百分比显示
        startangle=120,
        radius=1.2,
        wedgeprops={'linewidth': 1.5, 'edgecolor': 'green'}, #设置饼图的内外边界属性值
        textprops={'fontsize': 10, 'color': 'black'},  #设置文本标签的属性
        );
# 设置图形标题
plt.title('用户教育水平分布')
# 显示
plt.show();
