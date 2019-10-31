#!/bin/python
# 第8周作业第5道程序题——分段函数实现
x = eval(input())
y = 0
if x < 0:
    y = abs(x)
if 0 <= x < 5:
    y = x
if 5 <= x < 10:
    y = 3 * x - 5
if 10 <= x < 20:
    y = pow(x, 2) - 2
if x >= 20:
    y = 0
print(y)
