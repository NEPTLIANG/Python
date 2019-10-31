#!/bin/python
# 第8周作业第3道程序题——函数计算乘积
def Multi(t):
    result = 1
    for item in t:
        if type(item) != int:
            return "输入的不是有效整数!"
        result *= item
    return result


t = eval(input())
print(Multi(t))
