#!/usr/bin/env python
# -*-coding:utf-8 -*-

def char_triangle(lines:int,ch:str='*') -> None:
    cnt = 1
    while cnt <= lines:
        print("{:^{width}}".format(ch*(cnt*2-1),width=lines*2-1))
        cnt += 1

def main():
    char_triangle(3)

if __name__=='__main__':
    main()