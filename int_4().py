# coding=gbk

# 实现将二进制IP地址转换为十进制表示的IP地址

def get_num(b):
	list_str = b.split(" ")
	new_str = []
	for i in list_str:
		new_str.append(str(int(i, 2)))
	return ".".join(new_str)
print(get_num("00001010 00000011 00001001 00001100"))

# 2021.5.2
