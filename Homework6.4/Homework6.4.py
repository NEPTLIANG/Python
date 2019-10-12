#!/bin/python
# 第6周第4道程序题——阶乘求和
n = eval(input())
result = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(i, 1, -1):
        factorial *= j
    result += factorial
print(result)
