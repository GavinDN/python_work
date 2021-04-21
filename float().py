# coding=gbk

# 功能：float()函数用于将整数和字符串转换为浮点数。
# 语法：float(x)

'''
参数说明：
x：整数或字符串。
返回值：返回浮点数；如果参数x未提供，则返回0.0。
提示：如果floatO函数的参数x是一个字符串，则参数x应该是一个十进制数字的字符串表示形式（即参数x必须为能正确转换成浮点型数值的形式），否则会提示ValueError 错误。
'''
print(float())      # 不提供参数，返回0.0，输出：0.0
print(float(-88))   # 将整数转换为浮点数，输出：-88.0 
print(float(10/3))  # 将运算结果转换为浮点数 
print(float(2019))  # 将整数转换为浮点数
