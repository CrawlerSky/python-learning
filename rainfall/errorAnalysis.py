#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 18:21
# @Author  : zengsk in HoHai
# @File    : errorAnalysis.py

import os
import re
import numpy as np
import pandas as pd
import warnings

warnings.simplefilter("ignore")

# data source
maskFile = r"D:\work\code\mask\mask_china_cmp.txt"
sMatchFile = r"D:\work\code\match\matched_gpm_hourly_summ.txt"
gMatchFile = r"D:\work\code\match\matched_cmpa_hourly_summ.txt"

mask = pd.read_table(maskFile, sep="\s+", header=None, skiprows=6).values
with open(sMatchFile, "r") as sFid:
    sPaths = [line.strip() for line in sFid.readlines()]
with open(gMatchFile, 'r') as gFid:
    gPaths = [line.strip() for line in gFid.readlines()]

# The number of grids in the study region
ngirds = np.sum(mask>=0)

# read rainfall
sPrecip = [];
gPrecip = [];
for sfile in sPaths:
    rain = pd.read_table(sfile, sep="\\s{2,}|\t").values
    sPrecip.append(rain)
for gfile in gPaths:
    rain = pd.read_table(gfile, sep="\s+").values
    gPrecip.append(rain)

# Calculate the average rainfall per grid


