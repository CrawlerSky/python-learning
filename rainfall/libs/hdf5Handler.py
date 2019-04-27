#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 22:27
# @Author  : zengsk in HoHai
# @File    : hdf5Handler.py

import os
import numpy as np
import pandas as pd
import h5py

# 获取文件的所有属性信息
def chkAttrs(filename):
    f = h5py.File(filename, 'r')
    if len(f.attrs.items()):
        print("{} contains: ".format(filename))
        print("Global Attributes:")
    for key, value in f.attrs.items():
        print("----{}:".format(key))
        GlobalAttrs = str(value, encoding="utf-8");
        print(GlobalAttrs)  # 输出储存在File类中的attrs信息，一般是各层的名称

    # 读取各层的名称以及包含层信息
    for LyrName, layer in f.items():
        print("  {}".format(LyrName))
        print("    Attributes:")
        for key, value in layer.attrs.items():  # 输出储存在Group类中的attrs信息，一般是各层的weights和bias及他们的名称
            print("----{}:".format(key))
            lyrAttrs = str(value, encoding="utf-8")
            print(lyrAttrs)
        # 读取各层储存的datasets及其维度
        print("    Dataset:")
        for varName, ds in layer.items():
            print("      {}: {}".format(varName, ds.value.shape))  # 输出储存在Dataset中的层名称和维度

# 查看HDF5文件的包含的数据集
def chkDatasets(filename):
    f = h5py.File(filename, 'r')
    for LyrName, layer in f.items():
        # 读取各数据层的属性信息
        for key, value in layer.attrs.items():
            print("/{} {}:".format(LyrName, key))
            LyrAttrs = str(value, encoding="utf-8")
            print(LyrAttrs)
        # 读取各数据层中储存的Dataset数据集
        print("Datasets:")
        for varName, ds in layer.items():
            print("/{}/{}: {}".format(LyrName, varName, ds.value.shape))  # 输出储存在Dataset中的层名称和维度

# 读取HDF5文件中指定的数据集
def read_hdf5(filename, varName):
    f = h5py.File(filename, 'r')
    return f[varName]

