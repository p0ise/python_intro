#!/usr/bin/env python
# -*-coding:utf-8 -*-

def main():
    num = int(input("请输入一个数n>"))
    print("冰雹序列：")
    cnt = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num*3 + 1

        cnt +=1
        print("{:>5d}, ".format(num), end='')

        if cnt%10==0:
            print()

    print("\n冰雹序列长度为：%d"%cnt)


if __name__ == "__main__":
    main()
