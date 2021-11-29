#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""calculate 7/911 preciously to 1000 after point
"""
from decimal import *

getcontext().prec = 1000
a = Decimal(7)
b = Decimal(911)
print(a/b)
