#!/usr/bin/env python
# -*-coding:utf-8 -*-

def main():
    for row in range(1,10):
        for column in range(1,row+1):
            print("{:d}*{:d}={:<2d}".format(row, column, row*column), end="  ")
        print()
    
if __name__=='__main__':
    main()