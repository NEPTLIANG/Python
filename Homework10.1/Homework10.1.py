#!/bin/python
# 第10周程序题1——输出学生基本信息

# 补充下列代码
class Student:
    def __init__(self, name, gender, age, address):
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address

    def display(self):
        print("{}，{}，{}岁，{}。".format(self.name, self.gender, self.age, self.address))


tmp = eval(input())
s1 = Student(*tmp)
s1.display()
