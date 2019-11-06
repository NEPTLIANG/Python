#!/bin/python
# 第9周程序题1——统计随机整数出现的频率
import random

dict1 = {}
random.seed(10)
for i in range(1, 21):
    dict1[i] = 0
for num in range(0, 50):
    randomNum = random.randint(1, 20)  # randint方法返回随机整数，注意randint的范围是闭区间
    dict1[randomNum] += 1
for i in range(1, 21):
    if dict1[i] == 0:
        del dict1[i]
        i -= 1
    else:
        print("{} {}".format(i, dict1[i]))
