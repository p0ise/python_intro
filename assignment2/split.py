#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""split the line of test file into four lines
"""

filename = "test"
content = ""
with open(filename, mode='r') as f:
    content = f.read().strip().split(' ')

content = '\n'.join([' '.join(content[i:i+5]) for i in range(0, 20, 5)])
with open("new", mode="w") as f:
    f.write(content)
