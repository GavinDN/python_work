# coding=gbk

# 功能：open()函数用于打开文件，返回一个文件读写对象，然后对文件进行相应读写操作
# 语法：open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=Ture, opener=None)

'''参数说明：file：必须参数，文件路径，表示需要打开文件的相对路径（相对于程序所在路径，例如，要创建或打开程序所在路径下的“mr.txt”，
则可以直接写成相对路径“mr.txt”，如果是程序所在路径下的“soft”子路径的“mr.txt”文件，则可写成“soft/mr.txt”）或者绝对路径
（需要输入包括盘符的完整文件路径，如“D：/mr.txt”）'''

'''mode：可选参数，用于指定文件的打开i模式。常见的打开模式由r（以只读模式打开）、w（以只写模式打开），a(以追加模式打开)，
默认的打开模式为只读（即r）。实际调用的时候可以根据情况进行组合'''

with open("D：/text.txt", "r") as f:                    # 以只读的方式打开文件
with open("D：/text.txt", "w") as f:                    # 以只写的模式打开文件
with open("D：/text.txt", "r", encoding="gbk") as f:    # 以只读的模式打开文件
	print(f.readlines())                               # 读取全部内容
file = open("D:/python,jpg", "rb")                     # 以二进制方式打开图片

# 2021.4.23
