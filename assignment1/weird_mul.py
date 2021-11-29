#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""a program for using the new multiplication by shell.
"""


def new_mul(a, b):
    """a new type of multiplication

    Args:
        a (int): a number for multiplication
        b (int): another number for multiplication

    Returns:
        int: the result of the multiplication
    """
    product = 0
    while b != 0:
        if b % 2 == 1:
            product += a
        a *= 2
        b //= 2

    return product


def is_continue():
    """ask if continue

    Returns:
        bool: whether continue
    """
    text = input("Do you want to continue([y]/n)?")
    if text == '':
        text = 'y'
    if text.lower() == 'y':
        return True
    else:
        return False


def main():
    # introduction
    init = "There is a werid multiplication called Russian Peasant or Ancient Egyptian.\n"\
           "Input two numbers, and I will show you how it work."
    print(init)

    # begin loop
    loop = True
    while loop:
        try:
            a = int(input("Please input a here>"))
            b = int(input("Please input b here>"))
        except:
            print("Error: Please input numbers correctly.")
            if is_continue():
                continue
            else:
                break

        product = new_mul(a, b)

        print(f"I got it! The multiplication result is {product}.")

        loop = is_continue()

    # end
    print("Thanks for using.")


if __name__ == "__main__":
    main()
