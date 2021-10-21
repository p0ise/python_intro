#!/usr/bin/env python
# -*-coding:utf-8 -*-

number_of_cars = 575*10000
waste_per_km = 150
average_distance = 15000
population = 2114*10000

total = number_of_cars*average_distance*waste_per_km/1000000
waste_per_person = total/population*1000000

print("2015年北京全年机动车排放废气%f吨"%total)
print("平均每人吸入%f克废气"%waste_per_person)