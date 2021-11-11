#!/usr/bin/env python
# -*-coding:utf-8 -*-

def main():
    text = input("Please input a string>")
    result = ""
    search = list("aeiou")
    cnt = 0
    for index,ch in enumerate(text.lower()):
        if ch in search:
            search.remove(ch)
            result += ch
            cnt = index + 1
            if not search:
                break
    
    if search:
        print("[-]Couldn't get all five vowels in the given string.")
    else:
        print("[+]It took %d times to get all five vowels."%cnt)

if __name__=="__main__":
    main()