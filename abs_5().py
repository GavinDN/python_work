# coding=gbk

# 利用绝对值比较大小并输出较大者

# 编写程序，输入两个负数并比较它们的大小，同时输出较大者，代码如下：

a = int(input('请您输入一个负数:'))
b = int(input('请再输入一个负数:'))

# 绝对值大的负数反而小

if abs(a)>abs(b):
	print(b)
else:
	print(a)
