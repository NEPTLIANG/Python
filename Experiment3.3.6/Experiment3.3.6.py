#!/bin/python
# 实验3内容3(6)
upper1 = 2
upper2 = 3
under1 = 1
under2 = 2
result = upper1 / under1 + upper2 / under2
for i in range(20):
    upper = upper1 + upper2
    upper1 = upper2
    upper2 = upper
    under = under1 + under2
    under1 = under2
    under2 = under
    result += upper2 / under2
print(result)
