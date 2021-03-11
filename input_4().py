# coding=gbk

try:
	year = int(input("请输入一个年份："))
	# 能被4整除但不能被100整除
	if year % 4 == 0 and year % 100 != 0:
		print(year,"是闰年！")
	# 能被4整除
	elif year % 400 == 0:
		print(year,"是闰年！")
	else:
		print(year,"不是闰年！")
except:
	print("请不要输入与数值无关的数据！")
