# 第三章测试题

"""
第1、2题
get_list = []
x = int(input("请输入一个要求平方的数："))
for i in range(3):
	get_nums = (int(input("请输入要求最值的3个数:")))
	get_list.append(get_nums)

# output = pow(get_list[-1], 2)
max_num = max(get_list)
min_num = min(get_list)
print("这个数的平方是：%d" % pow(x, 2))
print("这组数的最大值为%d，最小值为%d" % (max_num, min_num))
"""


"""
第3题
get_list = []
for i in range (5):
	get_list.append(int(input("请输入元素：")))
print([get_list[1], get_list[3]])
print(get_list[1:4:2])
"""

"""
第5题
get_sorce = input("请输入学生的分数：")
get_list = get_sorce.split(",")
get_list = [int(get_list[i]) for i in range(len(get_list))]
sum_sorce = sum(get_list)
avg_sorce = sum_sorce/len(get_list)
print("总分：%d" "平均分：%d" % (sum_sorce, avg_sorce))
"""

# 第四章

# 第53页 例4-10 打印出指定范围内的素数
"""x = (int(input("请输入开始值：")), int(input("请输入结束值：")))
x1 = min(x)
x2 = max(x)
for n in range(x1, x2+1):
	for i in range(2, n-1):
		if n % i == 0:
			break
	else:
		print(n, "是素数")"""

# 第55页 例4-11 使用while循环实现遍历
"""alist = [1, 2, 3, 4, 5]
total = len(alist)
i = 0
while i  < total:
	print(alist[i], "的平方是：",alist[i]*alist[i])
	i = i + 1
else:
	print("循环结束！")"""

# 第51页 例4-7 for循环
"""for i in [6,7,8,9,10]:
	if i == 2:
		continue
	print(i,"的平方是：", i*i)
	if i == 7:
		break
else:
	print("循环结束！")"""

# 第58页 第1题
"""sorce = [int(input("请输入第一门成绩：")), \
	int(input("请输入第二门成绩："))]
if sorce[0] >= 60:
	print("通过！")
	if sorce[1] < 60:
		print("补考！")
else:
	print("未通过！")"""

# 第58页 第3题
"""
list = []
list = input("请输入20个数据：").split()
zlist = [int(i) for i in list if int(i) > 0]
flist = [int(i) for i in list if int(i) < 0]
print("正数有：", zlist)
print("负数有：", flist)
"""

# 第72页 第1题
"""
list = list(input("请输入要排序的列表：").split(" "))
def order(list=None):
	list.sort()
	print(list)


if __name__ == '__main__':
	order(list)
"""


# 第72页 第2题
"""
str = input("请输入字符串：")
def count_str(str=None):
	num = str.count(" ")
	print(num)


if __name__ == '__main__':
	count_str(str)
"""


# 第72页 第4题
"""
name = input("请输入姓名：")
password = input("请输入密码：")
def log_in(name, password, usertype=None, **kwas):
	if name == "john":
		if password == "2354kdd":
			print("登录成功！")
		else:
			print("密码输入错误！")
	else:
		print("没有此用户的信息！")


if __name__ == '__main__':
	log_in(name, password)
"""


# 第六章
# 第79页 实例6-5
# 类属性和实例属性的理解
'''
class Demo_Property(object):
	"""docstring for Demo_Property"""
	class_name = "Demo_Property"
	def __init__(self, x=0):
		self.x = x
	
	def class_info(self):
		print('类变量值：',Demo_Property.class_name)
		print('实例变量值：', self.x)

	def chng(self, x):
		self.x = x

	def chng_cn(self, name):
		Demo_Property.class_name = name


def main():
	dpa = Demo_Property()
	dpb = Demo_Property()
	print('初始化两个实例')
	dpa.class_info()
	dpb.class_info()
	print('修改实例变量')
	print('修改dpa实例变量')
	dpa.chng(3)
	dpa.class_info()
	dpb.class_info()
	print('修改dpb实例变量')
	dpb.chng(10)
	dpa.class_info()
	dpb.class_info()
	print('修改类变量')
	print('修改dpa类变量')
	dpa.chng_cn('dpa')
	dpa.class_info()
	dpb.class_info()
	print('修改dpb类变量')
	dpb.chng_cn('dpb')
	dpa.class_info()
	dpb.class_info() 


if __name__ == '__main__':
	main()
'''


# 第82页 例6-7
# 第85页 第2题
# 类的继承理解
'''
class Ant(object):
	"""docstring for FlyAnt"""
	def __init__(self, x=0, y=0, color='black'):
		self.x = x
		self.y = y
		self.color = color

	def  crawl(self, x=0, y=0):
		print('爬行。。。')
		self.x += x
		self.y += y
		self.info()

	def info(self):
		print('当前位置：(%d, %d)' % (self.x, self.y))

	def attack(self):
		print("用嘴咬！")

	def __eat(self):
		print("吃。。。")


class FlyAnt(Ant):

	def attack(self):
		print('用尾针！')

	def fly(self, x=0, y=0):
		print('飞行。。。')
		self.x += x
		self.y += y
		self.info()


class FinalAnt(FlyAnt):
	
	def leap(self, x=0, y=0):
		print('跳跃。。。')
		self.x += x
		self.y += y
		self.info()	

if __name__ == '__main__':
	
	flyant = FlyAnt(color='red')
	flyant.crawl(3,5)
	flyant.fly(10,14)
	flyant.attack()

	# 子类flyant没有父类的__eat()方法
	# flyant.eat()
	print("实例化出finalant对象")
	finalant = FinalAnt()
	finalant.leap(3, 4)
	finalant.crawl(1, 2)
	finalant.fly(1, 1)
'''

