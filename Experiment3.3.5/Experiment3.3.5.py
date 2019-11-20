#!/bin/python
# 实验3内容3(5)
n = eval(input())
if n % 2:
    for row in range(1, n + 1):
        if row < (n / 2):
            print("{:^20}".format("*" * (2 * row - 1)))
        else:
            print("{:^20}".format("*" * (2 * (n - row) + 1)))
