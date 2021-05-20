# coding=gbk

# 将字典转换为字符串形式

# 在使用str()方法将字典转换为字符串形式，代码如下：

mydic = {'Python图书': {'1':'零基础学Pyhton', '2':'Python从入门到项目实践', '3':'Python项目开发案例集锦', '4':'Python编程锦囊'}}
mystr = str(mydic)  # 字典转换为字符串
print(mystr)        # 输出字符串
print(type(mystr))  # 查看类型
