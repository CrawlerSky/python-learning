#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 17:28
# @Author  : zengsk in HoHai

import os
import sys
from ftplib import FTP

# 连接ftp服务器
def ftpConnect(ftpserver, port, usrname, password):
    ftp = FTP()
    try:
        ftp.connect(ftpserver, port)
        ftp.login(usrname, password)
    except:
        raise IOError('\n FTP connection failed, please check the code!')
    else:
        print(ftp.getwelcome()) # 打印登陆成功后的欢迎信息
        print('\n+------- ftp connection successful!!! --------+')
        return ftp

# 下载单个文件
def ftpDownloadFile(ftp, ftpfile, localfile):
    # fid = open(localfile, 'wb') # 以写模式打开本地文件
    bufsize =  1024
    with open(localfile, 'wb') as fid:
        ftp.retrbinary('RETR {0}'.format(ftpfile), fid.write, bufsize) # 接收服务器文件并写入本地文件
    return True

# 下载整个目录下的文件
def ftpDownload(ftp, ftpath, localpath):
    print('Remote Path: {0}'.format(ftpath))
    if not os.path.exists(localpath):
        os.makedirs(localpath)
    ftp.cwd(ftpath)
    print('+---------- downloading ----------+')
    for file in ftp.nlst():
        print(file)
        local = os.path.join(localpath, file)
        if os.path.isdir(file):           # 判断是否为子目录
            if not os.path.exists(local):
                os.makedirs(local)
            ftpDownload(ftp, file, local) # 递归调用
        else:
            ftpDownloadFile(ftp, file, local)
    ftp.cwd('..')
    ftp.quit()
    return True

# 退出ftp连接
def ftpDisConnect(ftp):
    ftp.quit()
        
        
# 程序入口
if __name__ == '__main__':
    # 输入参数
    ftpserver = 'jsimpson.pps.eosdis.nasa.gov'
    port = 21
    usrname = 'zengsk1010@gmail.com'
    pwd = 'zengsk1010@gmail.com'
    ftpath = '/NRTPUB/imerg/late/201403/'
    localpath = 'D:/data/'

    
    ftp = ftpConnect(ftpserver, 21, usrname, pwd)
    flag = ftpDownload(ftp, ftpath, localpath)
    print(flag)
    ftpDisConnect(ftp)
    print("\n+-------- OK!!! --------+\n")

    
# FTP相关操作：
'''
    from ftplib import FTP            # 加载ftp模块
    ftp=FTP()                         # 设置变量
    ftp.connect("IP","port")          # 连接的ftp sever和端口
    ftp.login("user","password")      # 连接的用户名，密码
    ftp.getwelcome()                  # 欢迎信息

    ftp.set_debuglevel(2) # 打开调试级别2，显示详细信息
    ftp.set_debuglevel(0) # 关闭调试模式
    ftp.getwelcome()      # 登陆成功后打印欢迎信息
    ftp.cwd(ftpath)       # 设置ftp当前操作的路径
    ftp.dir(ftpath)       # 显示目录下所有文件的详细信息
    ftp.nlst(ftpath)      # 获取目录下的文件
'''









