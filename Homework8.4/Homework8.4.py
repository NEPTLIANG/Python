#!/bin/python
# 第8周作业第4道程序题——函数判断质数

# 补充下列语句
def isPrime(num):
    if num == 0 or num == 1:
        return "False"
    for smallNum in range(2, num):
        if num % smallNum == 0:
            return "False"
    return "True"


num = eval(input())
print(isPrime(num))
