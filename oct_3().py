# coding=gbk

# 实现键盘字符串八进制对照表功能

# 使用oct()函数实现键盘字符八进制对照表功能，即按下键盘上指定的字符串后自动转换为八进制字符串形式
import binascii      # 导入binascii 模块
def contrast8(mystr):
	val16 = binascii.hexlify(mystr.encode('gbk'))
	val10 = int(val16.upper(), 16)
	val8  = oct(val10)
	return val8
# 接收用户输入的字符，返回该字符对应的八进制形式
while 1:
	mystr1 = input('请输入一个有效的字符：')  # 提示输入一个有效的字符
	print(contrast8(mystr1))
	
