#!/bin/python
# 实验5内容3(3)——猜数字游戏
guess = 0
secret = 7
times = 1
print('--------欢迎参加猜数字游戏，请开始--------')
while guess != secret:
    guess = int(input("请输入0-9之间的数字："))
    print("你输入的数字是：", guess)
    if guess == secret:
        print('你猜了{}次，猜对了，真厉害'.format(times))
    elif guess < secret:
        print('你猜的数字小于正确答案')
    else:
        print('你猜的数字大于正确答案')
    times += 1
print('game over')
