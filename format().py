# coding=gbk

# ���ܣ�format()�������Զ����ݽ��и�ʽ���������
# �﷨��format(value, format_spec)
# format_specΪ��ʽ�����ͣ�������format_specΪ��ʱ����ͬ��str(value)�ķ�ʽ
# valueΪҪת��������

print(format(3.14, 'f'))             # ת���ɸ�������Ĭ��ΪС�����6λ
print(format(52, '4d'))              # 8λ������ʾ�����㲿������ǰ�ÿո����
print(format(123, '.2f'))            # ��ʽ��Ϊ����2λС���ĸ�����
print(format(0.61896, '%'))          # ��С����ʽ��Ϊ�ٷ���
print('$' + format(123.2341, '.2f')) # �����Ԫ���ţ�С������2λ 
print(format('Gavin', '6^11.5'))     # ��ȡ�����ַ������Ϊ10���У������á�M�����
print(format(0xff, 'd'))             # ʮ������ת����ʮ����

