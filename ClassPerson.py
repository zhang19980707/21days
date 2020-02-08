class Person(object):
    """person类"""
    def __init__(self, name, brithday, height, weight):
        self.name = str(name)
        self.brith = brithday
        self.height = int(height)
        self.weight = int(weight)

    def person_info(self):
        year = int(self.brith[0:4])  # 字符串切片切片操作str[start:end:step]
        print("姓名：%s" % self.name)
        print("出生年份%d年" % year)
        print("年龄：%d岁" % (2020-year))
        print("身高:", self.height)
        print("体重：", self.weight)

    def standard(self):
        max_s = self.height - 90
        min_s = self.height - 110
        if self.weight <= max_s or self.weight >= min_s:
            print("体重合格")
        else:
            print("体重不合格")


if __name__ == '__main__':
    xiaoming = Person("小明", "1998年12月9号", 183, 78)
    xiaoming.person_info()
    xiaoming.standard()
