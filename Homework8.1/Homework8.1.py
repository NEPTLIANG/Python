#!/bin/python
# 第8周作业第1道程序题——计算时间的下一秒

# 完成下列函数体代码
def nextsecond(hour, minute, second):
    second += 1
    if second >= 60:
        second = second % 60
        minute += 1
    if minute >= 60:
        minute = minute % 60
        hour += 1
    hour %= 24
    return hour, minute, second


if __name__ == "__main__":
    h, m, s = map(int, input().split())
    print(*nextsecond(h, m, s), sep=' ')
