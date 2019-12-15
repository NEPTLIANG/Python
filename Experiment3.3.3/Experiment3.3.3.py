#!/bin/python
# 实验3内容3(3)
n = eval(input("n = "))
a = eval(input("a = "))
num = 0
result = 0
record = []
for i in range(0, n):
    num += a * 10 ** i
    result += num
    record.append(num)
print(record)
print(result)
