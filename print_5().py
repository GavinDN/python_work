# coding=gbk

# 进制输出

x=112

print("八进制数：%o"%x)                             # 使用操作符输出八进制
print("十六进制数：%x"%x)                           # 使用操作符输出十六进制
print("nHex = %x, nDec = %d, n0ct = %o"%(x,x,x))  # 输出十六进制、十进制、八进制数
print(bin(x))                                     # 使用bin()函数输出二进制数
print(oct(x))                                     # 使用oct()函数输出八进制数
print(hex(x))                                     # 使用hex()函数输出十六进制数
