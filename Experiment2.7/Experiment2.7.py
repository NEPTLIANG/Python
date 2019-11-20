#!/bin/python
# 实验2内容7
info = [["张三", 15, "男", 7, 2, 3.8],
        ["李四", 16, "女", 8, 1, 4.3]]
info.append(["王五", 15, "男", 8, 2, 4.2])
info.insert(0, ["赵六", 17, "女", 8, 1, 3.9])
grade = []
for person in info:
    print("%s的信息是：\n%d岁，%s性，%d年级%d班，成绩：%.1f" % (person[0], person[1], person[2], person[3], person[4], person[5]))
    grade.append(person[5])
grade.sort()
print("排序后：")
print(grade)
