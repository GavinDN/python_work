# coding=gbk

# 输出绝对值不大于3的所有整数

# 输出绝对值不大于3的所有整数，代码如下：

list = [-3, -2, -1, 0, 1, 2, 9]   # 创建一组整数列表
for num in list:                  # 遍历列表元素
	if abs(num)<=3:           # 绝对值不大于3
		print(num)        # 输出结果
