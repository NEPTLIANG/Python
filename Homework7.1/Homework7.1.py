#!/bin/python
# 第6周程序题1——计算100以内偶数的和
sumOfElement = 0
j = 0
for i in range(0, 101):
    if i % 2 == 0:
        sumOfElement += i
        j += 1
        # print("正在计算第" + str(j) + "个偶数:" + str(i) + "\n")
        print("第" + str(j) + "个偶数为:" + str(i))
print("100以内的偶数和为： " + str(sumOfElement))
