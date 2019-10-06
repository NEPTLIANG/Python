#!/bin/python
lst = eval(input())
indexOfItem = 0
while indexOfItem < len(lst):
    if lst[indexOfItem] % 2 == 0:
        lst[indexOfItem] = lst[indexOfItem] ** 2
    indexOfItem += 1
print(lst)
