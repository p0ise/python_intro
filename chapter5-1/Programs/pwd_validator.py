#!/usr/bin/env python
# -*-coding:utf-8 -*-
from getpass import getpass

def limit(text:str, least:int=None, most:int=None) -> bool:
    ret = True
    if least!=None and len(text)<least:
        ret = False
    if most!=None and len(text)>most:
        ret = False
    
    return ret


def validator(password:str) -> bool:
    ret = False
    count_number = 0
    count_lower = 0
    count_upper = 0
    if limit(password, 6, 20):
        for ch in password:
            if ch.isdigit():
                count_number += 1
            elif ch.islower():
                count_lower += 1
            elif ch.isupper():
                count_upper += 1
        
        if count_number and count_lower and count_upper:
            ret = True

    return ret

def confirm(pwd1:str, pwd2:str) -> bool:
    return pwd1==pwd2


def main():
    user_name = input("请输入您的用户名:")
    password = getpass("请输入您的密码（至少要有1个大写字母、1个小写字母和1个数字）:")
    if validator(password):
        re_password = getpass("请再次输入确认您的密码:")
        if confirm(password, re_password):
            print("设置成功！")
        else:
            print("验证失败！")
    else:
        print("密码不可用！")

if __name__=="__main__":
    main()