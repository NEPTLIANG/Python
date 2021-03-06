#!/bin/python
# 实验5内容3(6)——猜数字游戏之续了又续
import random


def guess_secret(max_times):
    secret = random.randint(0, 101)
    times = 1
    print('  ----------------------------------\n'
          '  ---                            ---\n'
          '  ---   欢迎参加猜数字游戏，请开始   ---\n'
          '  ---                            ---\n'
          '  ----------------------------------')
    for max_times in range(max_times, 0, -1):
        guess = int(input('请输入0-100之间的数字：'))
        print("你输入的数字是：", guess)
        if guess == secret:
            print('你猜了{}次，猜对了，真厉害'.format(times))
            break
        elif guess < secret:
            print('你猜的数字小于正确答案，还有%d次机会' % (max_times - 1))
        else:
            print('你猜的数字大于正确答案，还有%d次机会' % (max_times - 1))
        times += 1
    print('game over')


maxts = eval(input("@请输入猜数字的最大次数："))
guess_secret(maxts)
