#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""split the line of test file into four lines
"""

filename = "test"
with open(filename, mode='r+') as f:
    content = f.read().strip().split(' ')
    f.seek(0)
    f.truncate()
    content = '\n'.join([' '.join(content[i:i+5]) for i in range(0, 20, 5)])
    f.write(content)
