#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 18:34
# @Author  : zengsk in HoHai
# @File    : Calc_Avg_GSMaP.py

'''
Calculating the average precipitation over a given region
 GsMaP info:
    60N-->60S, 0-->360E;
    0.1*0.1degree;
    1 hourly or daily;
    4-byte-float;
'''

import os
import struct
import numpy as np
import pandas as pd
import warnings

warnings.simplefilter("ignore")

# header
header = '''ncols         3600
nrows         1200
xllcorner     0
yllcorner     -60
cellsize      0.1
NODATA_value  -999.0'''

# dataset directory
sPath = r'D:\data\GSMaP'

# mask region file
mask = pd.read_table(r'.\assets\china_mask_gpm_01.txt', sep='\s+', header=None, skiprows=6).values

rain = np.empty([1200, 3600], dtype=float)
tag = np.empty(rain.shape, dtype=float)     # Record the effective precip times per grid

Files = os.listdir(sPath)
for file in Files:
    filepath = os.path.join(sPath, file)
    if '.dat' == os.path.splitext(filepath)[1]:
        print(filepath)
        with open(filepath, 'rb') as fid:
            data = fid.read()
            data = struct.unpack('f'*3600*1200, data)
        data = np.array(data)
        data.resize(1200,3600)

        tag[data >= 0] = tag[data >= 0] + 1
        data[data < 0] = 0.0
        data *= 24           # unit conversion
        rain += data

# output
rainfall_avg = rain / tag
rainfall_avg[np.isnan(rainfall_avg)] = -999.00 # NODATA_value
rainfall_avg[mask<0] = -999.00

ofname = r'.\output\201607avg_gsmap.txt'
np.savetxt(ofname, rainfall_avg, fmt='%7.2f ', comments='', header=header)

print("\n+---------------- 数据处理完成!!! Nice Job!!! -----------------+\n")
