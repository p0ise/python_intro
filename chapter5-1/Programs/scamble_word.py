#!/usr/bin/env python
# -*-coding:utf-8 -*-
from random import sample


def scamble_word(text: str) -> str:
    ret = text[0]+''.join(sample(text[1:-1], len(text)-2))+text[-1]
    while len(ret)>3 and ret==text:
        ret = text[0]+''.join(sample(text[1:-1], len(text)-2))+text[-1]
    
    return ret

def main():
    word = input("请输入一个单词:")
    print("它的欺骗单词为:%s"%scamble_word(word))

if __name__=="__main__":
    main()
