# coding=gbk

n = input("输入一个字符：")         # 输出字母或数字，不能输入汉字
value = ord(n)                   # 用ord()函数将字符转换为对应的ASCII码值
print(n + "的ASCII码为：", value)  # 显示字符对应的ASCII码值
