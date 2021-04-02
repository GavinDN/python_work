# coding=gbk

# 将十进制数转换为二进制字符串并去掉前缀

def binary(n):
	s = bin(n)                          # 转换为二进制数
	print('%d 转换为二进制后%s' %(n, s))
	start = s.index('b') + 1            # 获取前缀的长度
	s = s[start:]
	print('去掉前缀为：%s' %(s))
binary(-36)                             # 负数
binary(10)                              # 正数
