#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Puzzle about how to replace the letters by numbers to make the equation true.
   Solved by dfs.
"""

data = "SEND+MORE=MONEY"

nums = {num: False for num in range(10)}
frequency = {}

for ch in data:
    if ch.isalpha():
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

# i think the more the letter appears, the greater its impact
# so i traverse them first
pripority = [k for k, v in sorted(frequency.items(), key=lambda x:x[1])]
answers = []


# recursion
def dfs(step):
    global data, pripority, answers
    left, right = data.split('=')
    a, b = left.split('+')
    # cut
    if '0' in (a[0], b[0], right[0]):
        return

    # stop condition
    if step == len(pripority):
        if int(a)+int(b) == int(right):
            answers.append(f'{a}+{b}={right}')
            return
    else:
        # enumerate all possible
        for value, is_used in nums.items():
            if not is_used:
                data = data.replace(pripority[step], str(value))
                nums[value] = True
                dfs(step+1)
                data = data.replace(str(value), pripority[step])
                nums[value] = False


def main():
    dfs(0)
    output_format = "{:-^15}"
    print(output_format.format('ANSWERS'))
    if answers:
        for line in answers:
            print(output_format.format(line))
    else:
        print(output_format.format('No Answer'))
    print(output_format.format("END"))


if __name__ == "__main__":
    main()
