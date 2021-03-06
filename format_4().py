# coding=gbk

# 进制转换

print(format(77))                   # 格式参数为空，默认为十进制数
print(format(77, 'd'))              # 原来是十进制数，转换后为原值
print(format(-77, 'd'))             # 原来是十进制数，转换后为原值
print(format(77, '8d'))             # 转换为8位十进制数，空余部分用空格填充
print(format(-77, '8d'))            # 转换为8位十进制数，负数在负号前填充空余部分空格
print(format(77, '+8d'))            # 转换为8位带符号十进制数，在符号前填充空余部分空格
print(format(-77, '08d'))           # 转换为8位十进制数，'0'在负号前填充空余部分空格
print(format(77, '+08d'))           # 转换为8位带符号十进制数，在符号前填充空余部分空格
print(format(-77, '#8b'))           # 转换为8位十进制数，加进制标志
print(format(-77, '=8d'))           # 转换为8位十进制数，空余部分填充空格
print(format(+77, '=8d'))           # 转换为8位十进制数，空余部分填充空格
print(format(+77, '*=8d'))          # 转换为8位十进制数，空余部分填充“*”
print(format(+77, '*=+8d'))         # 转换为8位带符号十进制数，符号与数据之间填充“*”
print(format(-77, '#=8d'))          # 转换为8位十进制数，在符号与空余部分填充“#”
print(format(+77, '*<8d'))          # 转换为8位十进制数，左对齐，空余部分填充“*”
print(format(-77, '#>8d'))          # 转换为8位十进制数，右对齐，空余部分填充“#”    
print(format(0x5a, 'd'))            # 十六进制数5a转换成十进制数
print(format(0b011101, 'd'))        # 二进制数011101转换成十进制数

# 2021/5/13
