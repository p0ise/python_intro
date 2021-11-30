#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""catch error
"""


def retry():
    """ask if retry

    Returns:
        bool: whether to retry
    """
    text = input("Do you want to try again([y]/n)?")
    if text == '':
        text = 'y'
    if text.lower() == 'y':
        return True
    else:
        return False


def main():
    # welcome
    print('input a,b,c and i will tell you the result of a/b*c')

    while True:
        try:
            a = int(input('a>'))
            b = int(input('b>'))
            c = int(input('c>'))
            print('[+]result is {}'.format(a/b*c))
        except ValueError:
            print("[-]Error:the input should be number!")
        except ZeroDivisionError:
            print("[-]Division 0 is meaningless.")
        finally:
            if retry():
                continue
            else:
                break

    # end
    print("Thank you for using, bye!")


if __name__ == "__main__":
    main()
