#!/bin/python
# 第7周作业程序题6——拆分数字
num = eval(input())
if num < 0:
    num = -num
g = num % 10
s = (num % 100) // 10
b = num // 100
print("{},{},{}".format(g, s, b))
