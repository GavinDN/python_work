# coding=gbk

# �ж��û�������ַ��Ƿ�Ϊ����

# �ж��û�������ַ��Ƿ�Ϊ���֣�������0~9������ʱ����ʾ����������֣���������ĸ�������ַ�ʱ������ʾ����Ƿ��ַ�
def Validate_Is_Number(val):                 # ����һ���ж��Ƿ�Ϊ���ֵĺ���
	getASCII = ord(val)                      # ���ַ�ת��Ϊ��Ӧ����ֵ
	if getASCII >= 48 and getASCII <= 57:    # �ж��Ƿ�Ϊ����
		return True
	else:
		return False
# �����û����룬�ж��Ƿ�Ϊ��������
while 1:
	getnum = input('������һ����Ч�����֣�0~9����')
	Is_Number = Validate_Is_Number(getnum)
	if Is_Number:
		print('�������������', getnum)
	else:
		print('�������˷Ƿ��ַ�������������')
