#!/bin/python
# 第9周程序题2——随机生成密钥
import random

m = eval(input())
n = eval(input())
sourceStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
random.seed(m)
for i in range(n):
    # key = ""
    # for char in range(0, 10):
    #     key += sourceStr[random.randint(0, 61)]  # 别忘了是闭区间
    # ----------------------------------------------------------------------
    # a = []
    # for char in range(0, 10):
    #     ch = random.choice(sourceStr)
    #     a.append(ch)
    a = random.choices(sourceStr, k=10)
    key = ''.join(a)
    print(key)
