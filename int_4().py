# coding=gbk

# ʵ�ֽ�������IP��ַת��Ϊʮ���Ʊ�ʾ��IP��ַ

def get_num(b):
	list_str = b.split(" ")
	new_str = []
	for i in list_str:
		new_str.append(str(int(i, 2)))
	return ".".join(new_str)
print(get_num("00001010 00000011 00001001 00001100"))
