# 根据分数给出成绩等级
score = eval(input("请输入你的成绩："))
# 此处输入你的程序
if score >= 90:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
print("输入成绩属于级别{}".format(grade))
