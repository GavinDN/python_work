# coding=gbk

# ʵ�ּ����ַ����˽��ƶ��ձ���

# ʹ��oct()����ʵ�ּ����ַ��˽��ƶ��ձ��ܣ������¼�����ָ�����ַ������Զ�ת��Ϊ�˽����ַ�����ʽ
import binascii      # ����binascii ģ��
def contrast8(mystr):
	val16 = binascii.hexlify(mystr.encode('gbk'))
	val10 = int(val16.upper(), 16)
	val8  = oct(val10)
	return val8
# �����û�������ַ������ظ��ַ���Ӧ�İ˽�����ʽ
while 1:
	mystr1 = input('������һ����Ч���ַ���')  # ��ʾ����һ����Ч���ַ�
	print(contrast8(mystr1))
	
