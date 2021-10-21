#!/usr/bin/env python
# -*-coding:utf-8 -*-

init = 90000
sum1 = init + 3.05/100*5*init
sum2 = init
for _ in range(5):
   sum2 += sum2*2.00/100
print("整存整取五年期总额：", sum1)
print("整存整取一年期总额：", sum2)
print("五年期收入：", sum1-init)