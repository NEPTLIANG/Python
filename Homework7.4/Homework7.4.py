#!/bin/python
# 第7周程序题4——列表中偶数位索引元素排序
inputList = eval(input())


def a(inputlist):
    sublist = []
    for i in range(0, len(inputlist)):
        if i % 2 == 0:
            sublist.append(inputlist[i])
    sublist.sort()
    for i in range(0, len(inputlist)):
        if i % 2 == 0:
            inputlist[i] = sublist[i // 2]
    print(inputlist)


a(inputList)
