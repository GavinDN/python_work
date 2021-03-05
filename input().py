# coding=gbk

# 功能：input()函数可以提示并接收用户的输入内容，将所有的输入内容按照字符串进行处理，并返回一个字符串
# 语法：input(prompt)
# 参数说明：prompt是可选参数，表示提示信息

score1 = int(input("请输入数学成绩："))         # 转换为整型
name = input("")                             # 无提示型输入，不换行
name = input("请输入您的名字：").strip(' ')     # 去除输入数据两端的空格
