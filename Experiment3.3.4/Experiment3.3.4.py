#!/bin/python
# 实验3内容3(4)
array = input("请输入身高（米）和体重（公斤）【半角逗号隔开】：").split(",")
height = eval(array[0])
weight = eval(array[1])
bmi = weight / height ** 2
international = "偏瘦"
national = "偏瘦"
if 18.5 < bmi < 25:
    international = "正常"
if 18.5 < bmi < 24:
    national = "正常"
if 25 < bmi < 30:
    international = "偏胖"
if 24 < bmi < 28:
    national = "偏胖"
if bmi >= 30:
    international = "肥胖"
if bmi >= 28:
    national = "肥胖"
print("BMI指数为：{:.2f}\nBMI指标为：国际'{}'，国内'{}'".format(bmi, international, national))  #.2后面要加f不然会变成科学计数法
