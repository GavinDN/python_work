# coding=gbk

# ���ܣ�open()�������ڴ��ļ�������һ���ļ���д����Ȼ����ļ�������Ӧ��д����
# �﷨��open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=Ture, opener=None)

'''����˵����file������������ļ�·������ʾ��Ҫ���ļ������·��������ڳ�������·�������磬Ҫ������򿪳�������·���µġ�mr.txt��,
�����ֱ��д�����·����mr.txt��������ǳ�������·���µġ�soft����·���ġ�mr.txt���ļ������д�ɡ�soft/mr.txt�������߾���·��
����Ҫ��������̷��������ļ�·�����硰D��/mr.txt����'''

with open("D��/text.txt", "r") as f:                    # ��ֻ���ķ�ʽ���ļ�
with open("D��/text.txt", "w") as f:                    # ��ֻд��ģʽ���ļ�
with open("D��/text.txt", "r", encoding="gbk") as f:    # ��ֻ����ģʽ���ļ�
	print(f.readlines())                               # ��ȡȫ������
file = open("D:/python,jpg", "rb")                     # �Զ����Ʒ�ʽ��ͼƬ
