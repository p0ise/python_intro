#!/usr/bin/env python
# -*-coding:utf-8 -*-

crude_reserve = 35.5*10000*10000
crude_import = 46188.5*10000
crude_consume = 63004.3*10000
crude_produce = 18932.4*10000

days_for_need = crude_reserve//(crude_consume - crude_produce)

print("中国的原油储备和自产原油可以维持%d天"%days_for_need)