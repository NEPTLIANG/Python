#!/bin/python
# 实验4内容3(4)
def maxnum(*nums):
    result = nums[0]
    for item in nums:
        if item > result:
            result = item
    return result


print(maxnum(-1, 34, -9, 56))
print(maxnum(1, 4, 6, 95, 3, 78))
