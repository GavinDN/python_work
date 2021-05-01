# coding=gbk

# 解决input()函数输入小数转换为整数出错的问题

myval = input('请输入小数：')
print(type(int(float(myval))))
