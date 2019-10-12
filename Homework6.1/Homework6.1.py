#!/bin/python
# 作业6第1题 a除以b
a = eval(input())
b = eval(input())
# print(str(a / b).format("{:.2}"))
if b != 0:
    print("{:.2f}".format(a / b))  # 大括号里要有个f否则只有一位小数
else:
    print("除零错误")
