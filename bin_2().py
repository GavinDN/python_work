# coding=gbk

# ��ʮ������ת��Ϊ�������ַ�����ȥ��ǰ׺

def binary(n):
	s = bin(n)                          # ת��Ϊ��������
	print('%d ת��Ϊ�����ƺ�%s' %(n, s))
	start = s.index('b') + 1            # ��ȡǰ׺�ĳ���
	s = s[start:]
	print('ȥ��ǰ׺Ϊ��%s' %(s))
binary(-36)                             # ����
binary(10)                              # ����
