#!/bin/python
# 实验4内容3(1)
def pyram(n):
    width = (n - 1) * 2 + 1
    for row in range(0, n):
        # print(" " * (n - row))
        # print("*" * (row * 2 + 1))
        # print('{:^' + n + '}'.fromat("*" * (row*2+1)))
        str = "*" * (row * 2 + 1)
        print(str.center(width))  # center(width, fillchar):返回一个指定的宽度width居中的字符串，fillchar为填充的字符，默认为空格


n = int(input("请输入行数n="))
pyram(n)
