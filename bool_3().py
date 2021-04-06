# coding=gbk

# 使用bool()函数验证数据

print("判断是否输入密码，如果返回值为False表示没有输入密码，否则表示输入了密码！")
x = input("请输入密码") 
print(bool(x.strip()))
x = input("请输入密码")
print(bool(x.strip()))
