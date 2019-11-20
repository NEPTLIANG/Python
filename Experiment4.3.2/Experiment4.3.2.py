#!/bin/python
# 实验4内容3(2)
def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


for n in range(1, 21):
    print('{:>2}!={}'.format(n, factorial(n)))
