def pingfang(x):
    """求平方函数"""
    print(x, "的平方是", pow(x, 2))


def jueduizhi(x):
    """求绝对值函数"""
    print(x, "的绝对值是", abs(x))


def sushu(x):
        for i in range(2, x):
            if x % i == 0:
                break
            print(x, "不是素数")
        else:
            print(x, "是素数")


if __name__ == '__main__':
    pingfang(2)
    jueduizhi(-0.2)
    sushu(2)
