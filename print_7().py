# coding=gbk

# ��̬ˢ�¿���̨���

import time                                        # ����ʱ��ģ��
for i in range(10, -1, -1):
	time.sleep(1)                                  # ����1��
	print("\r ����������� ".format(i), 'S', end='') # ������ݵ��ն�
