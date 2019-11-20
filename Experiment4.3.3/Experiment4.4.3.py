#!/bin/python
# 实验4内容3(3)
def fib(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return fib(n - 1) + fib(n - 2)


n = int(input('输入一个数n='))
print('n={0}, fib({0})={1}'.format(n, fib(n)))
