#!/bin/python
# 实验5内容3(4)——猜数字游戏续
import random

guess = -1
secret = random.randint(0, 101)
times = 1
print('--------欢迎参加猜数字游戏，请开始--------')
while guess != secret:
    guess = int(input("请输入0-100之间的数字："))
    print("你输入的数字是：", guess)
    if guess == secret:
        print('你猜了{}次，猜对了，真厉害'.format(times))
    elif guess < secret:
        print('你猜的数字小于正确答案')
    else:
        print('你猜的数字大于正确答案')
    times += 1
print('game over')
