# coding=gbk
class Rectangle():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def getPeir(self):
		print("�ܳ���%d" % ((self.x + self.y) * 2))
	def getArea(self):
		print("�����%d" % (self.x * self.y))
length = int(input("�����볤:"))
width = int(input("�������:"))
rect = Rectangle(length, width)
rect.getPeir()
rect.getArea()
