# coding=gbk

try:
	year = int(input("������һ����ݣ�"))
	# �ܱ�4���������ܱ�100����
	if year % 4 == 0 and year % 100 != 0:
		print(year,"�����꣡")
	# �ܱ�4����
	elif year % 400 == 0:
		print(year,"�����꣡")
	else:
		print(year,"�������꣡")
except:
	print("�벻Ҫ��������ֵ�޹ص����ݣ�")
