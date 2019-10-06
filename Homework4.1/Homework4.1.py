#!/bin/python
lst = eval(input())

# lengthOfList = len(lst)
# for indexOfElement in range(lengthOfList):
#     for indexOfAnotherElement in range(indexOfElement + 1, lengthOfList):
#         if lst[indexOfElement] == lst[indexOfAnotherElement]:
#             lst.pop(lst[indexOfAnotherElement])
#             lengthOfList -= 1

indexOfElement = 0
while indexOfElement < len(lst):
    indexOfAnotherElement = indexOfElement + 1
    while indexOfAnotherElement < len(lst):
        if lst[indexOfElement] == lst[indexOfAnotherElement]:
            lst.pop(indexOfAnotherElement)
        indexOfAnotherElement += 1
    indexOfElement += 1
print(lst)
