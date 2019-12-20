#!/bin/python
# 实验6内容3.5
from math import *


class MyPoint:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDdistance(self, p):
        return sqrt(pow((self.x - p.x), 2) + pow((self.y - p.y), 2))


p0 = MyPoint(2, 3)
print(p0.getX())
print(p0.getY())
p1 = MyPoint(5, 7)
print(p0.getDdistance(p1))
