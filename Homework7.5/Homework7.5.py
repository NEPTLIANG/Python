#!/bin/python
# 第7周程序题5——鸡兔同笼
n = eval(input())
for i in range(0, n):
    a = eval(input())
    if a % 2 == 0:
        minSum = (a // 4) + (a % 4) // 2
        maxSum = a // 2
        print("{} {}".format(minSum, maxSum))
    else:
        print("0 0")
