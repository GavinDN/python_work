# coding=gbk

# 判断用户输入的字符是否为数字

# 判断用户输入的字符是否为数字，当输入0~9的数字时，提示输入的是数字：当输入字母等其他字符时，则提示输入非法字符
def Validate_Is_Number(val):                 # 定义一个判断是否为数字的函数
	getASCII = ord(val)                      # 将字符转换为对应的数值
	if getASCII >= 48 and getASCII <= 57:    # 判断是否为数字
		return True
	else:
		return False
# 接收用户输入，判断是否为整型数字
while 1:
	getnum = input('请输入一个有效的数字（0~9）：')
	Is_Number = Validate_Is_Number(getnum)
	if Is_Number:
		print('您输入的是数字', getnum)
	else:
		print('您输入了非法字符，请输入数字')
