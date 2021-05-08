# coding=gbk

# 输出十进制数字的八进制字符串形式

# 输出0~10的八进制字符串型形式
i = 0                        # 变量i初始化为0
while i<11:                  # while循环条件
	print(oct(i),end = ' ')  # 使用oct()函数将变量i转换为八进制输出
	i += 1                   # 变量i自增
