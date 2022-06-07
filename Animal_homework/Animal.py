class Animal:
    """
    父类有属性：name, color, age, gender
    类方法：call run
    """
    # 姓名
    name = ""
    # 颜色
    color = ""
    # 年龄
    age = ""
    # 性别
    gender = ""

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def call(self):
        print(f"{self.name} is calling")

    def run(self):
        print(f"{self.name} is running")


# create class cat to extend animal
class Cat(Animal):

    # overriding __init__
    def __init__(self, name, color, age, gender):
        # 共性
        super().__init__(name, color, age, gender)
        # 个性
        self.furry = "short hair"

    # Add a new function--catch_mouse
    def Catch_mouse(self):
        print(f"{self.name} can catch mouse")

    # overriding call func
    def call(self):
        print(f"{self.name} is miao miao")


class Dog(Animal):

    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.furry = "long hair"

    def house_defend(self):
        print(f"{self.name} is defending house")

    def call(self):
        print(f"{self.name} is wang wang")


if __name__ == '__main__':
    # create a cat
    cat = Cat("Kitty cat", "black", "1", "female")
    # catch_mouse
    cat.Catch_mouse()
    print(f"姓名：{cat.name}, 年龄：{cat.age}, 性别：{cat.gender}, 毛发：{cat.furry}, 捉到了老鼠")

    # create a dog
    puppy = Dog("旺财", "金色", "2岁", "男狗")
    # house_defend
    puppy.house_defend()
    # print name color age gender furry
    print(f"姓名：{puppy.name}, 颜色：{puppy.color}, 年龄：{puppy.age}, 性别：{puppy.gender}, 毛发:{puppy.furry}")
