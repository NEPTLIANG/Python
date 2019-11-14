#!/bin/python
# 第10周程序题2——定义一个学生类

# 完成类体
class Student:
    def __init__(self, name, age, chinese, math, english):
        self.name = name
        self.age = age
        self.chinese = chinese
        self.math = math
        self.english = english

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        maxGrade = self.chinese
        if maxGrade < self.math:
            maxGrade = self.math
        if maxGrade < self.english:
            maxGrade = self.english
        return maxGrade


# 测试类中的方法
t = eval(input())
zm = Student(*t)
print(zm.get_name(), zm.get_age(), zm.get_course(), sep=' ')
