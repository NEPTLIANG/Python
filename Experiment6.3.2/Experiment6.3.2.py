#!/bin/python
# 实验6内容3.2
class Animal:
    @classmethod
    def show(cls):
        pass


class Bird(Animal):
    @classmethod
    def show(cls):
        print("我是一只红色的鸟\n今年2岁了！")


class Fish(Animal):
    @classmethod
    def show(cls):
        print("我是一只3斤重的鱼\n今年4岁了！")


Bird.show()
Fish.show()
