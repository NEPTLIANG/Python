#!/bin/python
# 实验6内容3.3
class Student:
    ch = -1
    ma = -1
    en = -1

    def input(self, ch, ma, en):
        self.ch = ch
        self.ma = ma
        self.en = en

    def output(self):
        sumofgrade = self.ch + self.ma + self.en
        print("总分：%d，平均分：%.1f" % (sumofgrade, sumofgrade / 3))


s1 = Student()
s1.input(93, 94, 95)
s1.output()
