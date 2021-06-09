# coding=gbk

# 获取可迭代对象中数字的绝对值

# 循环输出列表中定义的数字的绝对值，代码如下：

list = ['18', 12.45, 'ASD', 0, '考研加油', -19.69, '']   # 定义数字列表
for num in list:                                       # 遍历列表元素
	if isinstance(num, (int, float)):                  # 判断是否为数字
		print(abs(num))                                # 获取绝对值 
