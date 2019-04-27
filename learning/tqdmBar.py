#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 18:34
# @Author  : zengsk in HoHai

'''
python 好玩的进度条显示库tqdm:
        insall: pip install tqdm
        param:
            class tqdm(object):
                def __init__(self, iterable=None, desc=None, total=None):
        iterable: 可迭代对象，默认接受第一个参数,
        desc: 进度条前缀,
        total: 进度条长度.
'''

import time
from tqdm import tqdm

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    text = text + char
    time.sleep(0.1)


