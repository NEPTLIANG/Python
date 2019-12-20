#!/bin/python
# 实验6内容3.1
class Dog:
    name = ""
    color = ""
    weight = -1

    def __init__(self, name, color, weight):
        Dog.name = name
        Dog.color = color
        Dog.weight = weight

    def bark(self):
        return "wang！wang！"

    def show(self):
        print("一只体重为 {} 的 {} {} 在 wang！wang！叫".format(Dog.weight, Dog.color, Dog.name))


dog = Dog('旺财', '黄色', 10)
dog.show()
