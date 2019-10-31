#!/bin/python
# 第8周作业第2道程序题——判断IP地址合法性

# 补充函数体代码
def isLegalIP(s):
    listOfNum = s.split(".")
    if len(listOfNum) != 4:
        return "No"
    for item in listOfNum:
        if not item.isdigit():  # isdigit函数判断字符串是否只包含数字
            return "No"
        if eval(item) < 0 or eval(item) > 255:
            return "No"
    return "Yes"


if __name__ == "__main__":
    s = input()
    print(isLegalIP(s))
