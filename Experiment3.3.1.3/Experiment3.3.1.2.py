#!/bin/python
# 实验3内容3(1)第3种实现
x = eval(input())
if x < 0:
    y = -x / (x ** 2 + 1)
else:
    y = (x + 1) ** (1 / 2)
print(y)
