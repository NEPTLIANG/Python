#!/bin/python
# 实验6内容3.4
class Role:
    name = ""
    harm = -1
    skill = ""

    def commonAttack(self):
        print("{}使用了普通攻击，攻击力为{}".format(self.name, self.harm))

    def specialAttack(self):
        print("{}使用了技能攻击{}".format(self.name, self.skill))


class Guan(Role):
    name = "关羽"
    harm = 10
    skill = "单刀赴会"


class Lv(Role):
    name = "吕布"
    harm = 15
    skill = "贪狼之握"

    def specialAttack(self):
        self.speak()
        print("{}使用了技能攻击{}".format(self.name, self.skill))

    @staticmethod
    def speak():
        print("吕布：谁敢与战！！")


class Control:
    @staticmethod
    def main():
        playerGuan = Guan()
        playerLv = Lv()
        playerGuan.commonAttack()
        playerGuan.specialAttack()
        playerLv.commonAttack()
        playerLv.specialAttack()


Control.main()
