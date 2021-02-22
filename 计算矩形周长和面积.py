# coding=gbk
class Rectangle():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def getPeir(self):
		print("周长：%d" % ((self.x + self.y) * 2))
	def getArea(self):
		print("面积：%d" % (self.x * self.y))
length = int(input("请输入长:"))
width = int(input("请输入宽:"))
rect = Rectangle(length, width)
rect.getPeir()
rect.getArea()
