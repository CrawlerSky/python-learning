#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 22:00
# @Author  : zengsk in HoHai

'''
FTP批量下载数据
'''

import os
import sys
from ftplib import FTP

class FtpDownloadCls:
    def __init__(self, ftpserver, port, usrname, pwd):
        self.ftpserver = ftpserver # ftp主机IP
        self.port = port          # ftp端口
        self.usrname = usrname  # 登陆用户名
        self.pwd = pwd          # 登陆密码
        self.ftp = self.ftpConnect()

    # ftp连接
    def ftpConnect(self):
        ftp = FTP()
        try:
            ftp.connect(self.ftpserver, self.port)
            ftp.login(self.usrname, self.pwd)
        except:
            raise IOError('\n FTP login failed!!!')
        else:
            print(ftp.getwelcome())
            print('\n+------- FTP connection successful!!! --------+\n')
            return ftp

    # 单个文件下载到本地
    def downloadFile(self, ftpfile, localfile):
        bufsize = 1024
        with open(localfile, 'wb') as fid:
            self.ftp.retrbinary('RETR {0}'.format(ftpfile), fid.write, bufsize)
        return True

    # 下载整个目录下的文件,包括子目录文件
    def downloadFiles(self, ftpath, localpath):
        print('FTP PATH: {0}'.format(ftpath))
        if not os.path.exists(localpath):
            os.makedirs(localpath)
        self.ftp.cwd(ftpath)
        print('\n+----------- downloading!!! -----------+\n')
        for i, file in enumerate(self.ftp.nlst()):
            print('{0} <> {1}'.format(i, file))
            local = os.path.join(localpath, file)
            if os.path.isdir(file): # 判断是否为子目录
                if not os.path.exists(local):
                    os.makedirs(local)
                self.downloadFiles(file, local)
            else:
                self.downloadFile(file, local)
        self.ftp.cwd('..')
        return True

    # 退出FTP连接
    def ftpDisConnect(self):
        self.ftp.quit()


if __name__ == '__main__':
    # 输入参数
    ftpserver = 'hokusai.eorc.jaxa.jp' # ftp主机IP
    port = 21                          # ftp端口
    usrname = 'rainmap'       # 登陆用户名
    pwd = 'Niskur+1404'       # 登陆密码
    ftpath = '/standard/v7/daily/00Z-23Z/201507/'  # 远程文件夹
    localpath = 'D:/data/'                 # 本地文件夹

    Ftp = FtpDownloadCls(ftpserver, port, usrname, pwd)
    Ftp.downloadFiles(ftpath, localpath)
    Ftp.ftpDisConnect()
    print("\n+-------- OK!!! --------+\n")
    
        
    
    
