#!/usr/bin/env python
# -*-coding:utf-8 -*-

def char_triangle(n:int,ch:str='*') -> None:
    """Print a n-line triangle consisted of the given character."""
    cnt = 1
    while cnt <= n:
        print("{:^{width}}".format(ch*(cnt*2-1),width=n*2-1))
        cnt += 1

def main():
    char_triangle(10)

if __name__=='__main__':
    main()