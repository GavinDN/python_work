# coding=gbk

# 讲字节类型（bytes对象）转换为字符串形式

# 使用str()函数讲字节类型转换为字符串的形式，首先使用encode()方法对“明日科技”进行编码，输出字节类型，然后使用str()函数进行转换。代码如下：

s1 = '广东珠海'                       # 定义字符串
s2 = s1.encode(encoding = 'utf-8')   # 采用UTF-8编码
print(s2)                            # 输出字节类型
print(str(s2, encoding = 'utf-8'))   # 讲字节类型转换为字符串
