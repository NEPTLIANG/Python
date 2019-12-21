#!/bin/python
# 实验7内容3
from sqlite3 import *


def function1():
    addrBook = open("address.txt")
    print(addrBook.read())
    addrBook.close()


def function1ViaDB():
    dbstr = "addrBook.db"
    con = connect(dbstr)
    cur = con.cursor()
    cur.execute("SELECT * FROM addrBook;")
    for row in cur.fetchall():
        print("{},{},{},{}".format(row[0], row[1], row[2], row[3]))
    cur.close()
    con.close()


def function2():
    appendInfo = input("请输入要插入的信息，以逗号隔开，示例：113,zz,34567812,tianjing：") + "\n"
    addrBook = open("address.txt", "a")  # 模式a为追加模式
    addrBook.write(appendInfo)
    addrBook.close()


def function2ViaDB():
    appendInfo = input("请输入要插入的信息，以逗号隔开，示例：113,zz,34567812,tianjing：").split(",")
    dbstr = "addrBook.db"
    con = connect(dbstr)
    cur = con.cursor()
    cur.execute("INSERT INTO addrBook(no, name, tel, addr) VALUES(?, ?, ?, ?);",
                [appendInfo[0], appendInfo[1], appendInfo[2], appendInfo[3]])
    con.commit()  # 要提交事务才行
    for row in cur.execute("SELECT * FROM addrBook"):
        print("{},{},{},{}".format(row[0], row[1], row[2], row[3]))
    cur.close()
    con.close()


# Test case:
# 101,aa,12345678,Beijing
# 102,bb,23456781,shanghai
# 113,zz,34567,tianji
def function3():
    no = input("请输入要删除学生的学号：")
    # addrBook = open("address.txt", "r+")  # r+为读写模式，文件必须已存在否则报异常；w和w+模式会清空文件
    addrBook = open("address.txt")
    # infoList = addrBook.readlines()
    infoDict = {}
    for info in addrBook:
        info = info.split(",")
        infoDict[info[0]] = info
    while no not in infoDict.keys():
        no = input("当前学号不存在，请重新输入学号：")
    delAddress = open("del_address.txt", "w")
    # delAddress.close()
    # delAddress = open("del_address.txt", "a")
    delContent = ""
    for indexOfField in range(0, len(infoDict[no]) - 1):
        delContent += infoDict[no][indexOfField] + ","
    delContent += infoDict[no][len(infoDict[no]) - 1]
    delAddress.write(delContent)
    delAddress.close()
    infoDict.pop(no)
    addrBook.close()
    content = ""
    addrBook = open("address.txt", "w+")
    for record in infoDict.values():
        for indexOfField in range(0, len(record) - 1):
            content += record[indexOfField] + ","
        content += record[len(record) - 1]
    addrBook.write(content)
    # addrBook.flush()
    addrBook.close()  # 不知道为什么flush不行，要close掉重新open
    addrBook = open("address.txt")
    print(addrBook.read())
    addrBook.close()


def function3ViaDB():
    no = input("请输入要删除学生的学号：")
    dbstr = "addrBook.db"
    con = connect(dbstr)
    cur = con.cursor()
    cur.execute("SELECT * FROM addrBook;")
    isExist = False
    for row in cur.fetchall():
        if no == row[0]:
            isExist = True
    while not isExist:
        no = input("当前学号不存在，请重新输入学号：")
        cur.execute("SELECT * FROM addrBook;")
        for row in cur.fetchall():
            if no == row[0]:
                isExist = True
    delRow = cur.execute("SELECT * FROM addrBook WHERE no=?;", [no]).fetchone()
    cur.execute("INSERT INTO del_address(no, name, tel, addr) VALUES (?, ?, ?, ?);"
                , [delRow[0], delRow[1], delRow[2], delRow[3]])
    cur.execute("DELETE FROM addrBook WHERE no=?", [no])  # 别忘了参数要写在元组或列表里
    con.commit()
    for row in cur.execute("SELECT * FROM addrBook;"):
        print("{},{},{},{}".format(row[0], row[1], row[2], row[3]))
    cur.close()
    con.close()


print("1. 显示所有信息\n"
      "2. 追加信息\n"
      "3. 删除信息\n"
      "请输入数字 1-3 选择功能：", end="")
select = input()
while select != "1" and select != "2" and select != "3":
    print("请重新输入")
    select = input("请输入数字 1-3 选择功能：")
print("您选择了功能%s" % select)
# eval("function" + select + "()")
eval("function" + select + "ViaDB()")
