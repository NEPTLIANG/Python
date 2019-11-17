#!/bin/python
# 实验3内容3(2)
a = eval(input())
b = eval(input())
c = eval(input())
nb = b ** 2 - 4 * a * c
if a == 0 and b == 0:
    print("无解")
elif a == 0 and b != 0:
    print("x={}".format(-c / b))
elif nb == 0:
    print("x1=x2={}".format(-b / (2 * a)))
elif nb > 0:
    x1 = -b / (2 * a) + (b ** 2 - 4 * a * c) ** (1 / 2) / (2 * a)
    x2 = -b / (2 * a) - (b ** 2 - 4 * a * c) ** (1 / 2) / (2 * a)
    print("x1={}, x2={}".format(x1, x2))
elif nb < 0:
    nb1 = -b / (2 * a)
    nb2 = (4 * a * c - b ** 2) ** (1 / 2) / (2 * a)
    print("x1={0}+{1}i, x2={0}-{1}i".format(nb1, nb2))
