#!/usr/bin/env python
# -*-coding:utf-8 -*-

time_stamp = int(input("请输入总秒数>"))
print("24进制时间表示为%2d:%2d:%2d"%(time_stamp//3600, time_stamp//60%60, time_stamp%60))