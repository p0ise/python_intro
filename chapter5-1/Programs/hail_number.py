#!/usr/bin/env python
# -*-coding:utf-8 -*-
import turtle

def main():
    num = int(input("请输入一个数n>"))
    print("冰雹序列：")
    cnt = 0
    turtle.speed(10)
    turtle.goto(cnt*4, num*4)
    turtle.pendown()
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num*3 + 1

        cnt +=1
        print("{:>5d}, ".format(num), end='')
        turtle.goto(cnt*4, num*4)
        turtle.write(num)
        if cnt%10==0:
            print()

    print("\n冰雹序列长度为：%d"%cnt)
    input("Press an Enter to continue...")


if __name__ == "__main__":
    main()
