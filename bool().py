# coding=gbk

# 功能：bool是Boolean的缩写，只有真（True）和假（False）两种取值。bool（函数）只有一个参数，并根据这个参数的值返回真或假值。
# 语法：bool([x])

'''
参数说明：
x：要转换的参数，可以是数值、字符串、列表、元组等。
返回值：返回Ture或False。
	当bool()函数没有参数时，则返回False。
	当对布尔类型使用bool0函数时，则按原值返回。
	当对数字使用bool0函数时，0值返回False，其他值都返回True。
	当对字符串使用bool()函数时，对于没有值的字符（None或者空字符率）返回False，否则返回True。
	当bool()函数用于空的列表、字典、元组等对象时，则返回False，否则返回True。
注意：在Python中，除了"、""、0、()、[]、{}、None转换后返回值为False，其他转换后返回值都为True。也就是说字符串如果不为空，则永远转换为True。
说明：bool是int的子类。
'''

print(bool(0))                 # 将数字转换为bool类型
print(bool(None))              # 将None转换为bool类型
print(bool("2022，考研上岸！"))  # 将字符串转换为bool类型

