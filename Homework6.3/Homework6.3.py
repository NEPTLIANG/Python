#!/bin/python
# 第6周作业第3道程序题——阶乘
n = eval(input())
result = 1
for i in range(n, 1, -1):
    result *= i
print(result)
