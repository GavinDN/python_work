# coding=gbk

# 调整名字的大小写 
'''
将一个人名存储到一个变量中
再以大、小写和首字母大写的方式显示这个人名
'''

name = input("请输入您的姓名（英语）：")
print("以首个字母大写的形式输出：" + name.title())
print("以所有字母大写的形式输出：" + name.upper())
print("以所有字母小写的形式输出：" + name.lower())
