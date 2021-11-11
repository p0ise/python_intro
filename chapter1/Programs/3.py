#!/usr/bin/env python
# -*-coding:utf-8 -*-

popluation_2020 = 141178*10000
brith_rate = 8.52/1000
death_rate = 7.07/1000
brith_2021 = popluation_2020*brith_rate
dead_2021 = popluation_2020*death_rate
seconds_of_year = 365*24*3600           # 按一年365天计算
brith_per_second = brith_2021/seconds_of_year
death_per_second = dead_2021/seconds_of_year
print("2021年平均每秒有%d人出生，%d人死亡"%(brith_per_second, death_per_second))
print("2021年平均每%f秒有1人出生，每%f秒有1人死亡"%(1/brith_per_second, 1/death_per_second))