#!/bin/python
#第6周作业第6道程序题——计算阶乘
x = eval(input())
result = 1
for i in range(x, 1, -1) :
    result *= i
print(result)
