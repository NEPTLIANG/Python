#!/bin/python
# 实验5内容3(1)——拼手气红包
import random


def hongbao(total, num):
    each = []
    already = 0
    divide = []
    for i in range(1, num):  # 划分9次分成10份
        divide.append(random.random())
    divide.append(1)
    divide.sort()
    first = divide[0] * total  # 发出第1份
    # print("第1个：%f" % first)
    # add = first
    each.append(first)
    already += first
    for index in range(1, num):  # 发出第2~10份
        t = (divide[index] - divide[index - 1]) * total
        # print("第%d个：%f" % (index + 1, t))
        # add += t
        each.append(t)
        already += t
    # size = (1 - divide[num - 2]) * total  # 发出剩下的第10份
    # print("第%d个：%f" % (num, size))
    # sum += size
    # print("合计发出：%f" % add)  # 统计各份总数
    return each
    # get = random.random() * total
    # print(get)
    # total -= get


def test():
    for i in range(20):
        each = hongbao(20, 7)
        print('第{}种随机分配方案：'.format(i + 1), end="")
        print(*each, sep=",")


if __name__ == "__main__":
    test()
