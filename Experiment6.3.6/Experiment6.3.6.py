#!/bin/python
# 实验6内容3.6
from random import *

directionOption = ["x+", "x-", "y+", "y-"]


class GameAnimal:
    x = 0
    y = 0
    maxSpeed = -1
    speed = -1
    pow = -1
    consumptionOfPow = 0

    def __init__(self):
        self.initLocation()

    def initLocation(self):
        self.x = randint(0, 10)
        self.y = randint(0, 10)

    def move(self):
        self.speed = randint(1, self.maxSpeed)
        direction = directionOption[randint(0, 3)]
        # eval("self." + direction + "= self.speed")
        if direction == "x+":
            self.x += self.speed
        if direction == "x-":
            self.x -= self.speed
        if direction == "y+":
            self.y += self.speed
        if direction == "y-":
            self.y -= self.speed
        if self.x > 10:
            self.x = 10 - (self.x - 10)
        if self.x < 0:
            self.x = -self.x
        if self.y > 10:
            self.y = 10 - (self.y - 10)
        if self.y < 0:
            self.y = -self.y
        self.pow -= self.consumptionOfPow


class Tortoise(GameAnimal):
    maxSpeed = 2
    pow = 100
    consumptionOfPow = 1

    @staticmethod
    def eat(torX, torY):
        global fishes
        # seqNum = 1
        for fish in fishes:
            if torX == fish.x and torY == fish.y:
                tortoise.pow += 20
                print("第{}条鱼被吃掉了，其位置：({},{})，当前乌龟的体力为{}".
                      format(fishes.index(fish) + 1, fish.x, fish.y, tortoise.pow))
                fishes.remove(fish)
                # seqNum -= 1


class Fish(GameAnimal):
    maxSpeed = 1

    @staticmethod
    def moveAllFish():
        # global fishes
        # seqNumOfFish = len(fishes)
        for indexOfFish in range(len(fishes) - 1, -1, -1):
            fishes[indexOfFish].move()
            print("第{}条鱼移动后的位置：({},{})"
                  .format(indexOfFish + 1, fishes[indexOfFish].x, fishes[indexOfFish].y))
            fishes[indexOfFish].beEaten()
            # seqNumOfFish -= 1

    def beEaten(self):
        # global fishes
        if tortoise.x == self.x and tortoise.y == self.y:
            tortoise.pow += 20
            print("第{}条鱼被吃掉了，其位置：({},{})，当前乌龟的体力为{}"
                  .format(fishes.index(self) + 1, self.x, self.y, tortoise.pow))
            fishes.remove(self)


tortoise = Tortoise()
print("创建乌龟 初始位置：({},{})".format(tortoise.x, tortoise.y))
fishes = []
for indexOfFish in range(0, 10):
    fishes.append(Fish())
    print("创建第{}条鱼 初始位置：({},{})"
          .format(indexOfFish + 1, fishes[indexOfFish].x, fishes[indexOfFish].y))

while True:
    Fish.moveAllFish()
    tortoise.move()
    print("当前乌龟的移动步长：{}，移动后的位置：({},{})，当前体力：{}"
          .format(tortoise.speed, tortoise.x, tortoise.y, tortoise.pow))
    tortoise.eat(tortoise.x, tortoise.y)
    # torX = tortoise.x
    # torY = tortoise.y
    # eat(torX, torY)
    if not tortoise.pow:
        print("王八体力不支，累死了！")
        break
    if not len(fishes):
        print("鱼被王八吃完了，游戏结束")
        break
