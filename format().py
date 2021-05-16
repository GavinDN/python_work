# coding=gbk

# 功能：format()函数可以对数据进行格式化处理操作
# 语法：format(value, format_spec)
# format_spec为格式化解释，当参数format_spec为空时，等同于str(value)的方式
# value为要转换的数据

print(format(3.14, 'f'))             # 转换成浮点数，默认为小数点后6位
print(format(52, '4d'))              # 8位整数显示，不足部分整数前用空格填充
print(format(123, '.2f'))            # 格式化为保留2位小数的浮点数
print(format(0.61896, '%'))          # 将小数格式化为百分数
print('$' + format(123.2341, '.2f')) # 添加美元符号，小数保留2位 
print(format('Gavin', '6^11.5'))     # 截取三个字符，宽度为10居中，不足用“M”填充
print(format(0xff, 'd'))             # 十六进制转换成十进制


