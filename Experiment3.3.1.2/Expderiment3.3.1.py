#!/bin/python
# 实验3内容3(1)第2种实现
x = eval(input())
if x < 0:
    y = -x / (x ** 2 + 1)
if x >= 0:
    y = (x + 1) ** (1 / 2)
print(y)
