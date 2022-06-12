# 人类
import random


class Human:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def show(self):
        print(f"我是{self.name}, 我现在有{self.money}元")


# 群主类
class Manager(Human):

    def send(self, money, num):

        if self.money < money:
            print("余额不够")
            return None

        # 空的红包容器
        red_list = []
        # 扣钱
        self.money -= money

        # 瓜分算法
        avg = money // num  # 整除
        rest = money % num  # 余数
        # 平均数分给人数num
        for i in range(num):
            red_list.append(avg)

        # 将余数加到列表最后一个元素中
        red_list[-1] += rest
        return red_list


class member(Human):

    def grab(self, red_list: list):
        if not red_list:
            print("没有钱")
            return None

        random_index = random.randint(0, len(red_list) - 1)
        lucky_money = red_list.pop(random_index)
        print(f"{self.name}抢到了{lucky_money}")

        # 存钱
        self.money += lucky_money


if __name__ == '__main__':
    manager = Manager("kiko", 0)
    # 群主发红包
    reds = manager.send(20, 3)
    print(reds)

    tiffany = member("Tiffany", 70)
    tiffany.grab(reds)
    tiffany.show()
