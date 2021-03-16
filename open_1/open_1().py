 # coding=gbk
 
f = open("C:\Users\Gavin\Desktop\python_work\open_1\Gavin.txt") # 打开文件
lines = f.read(20000)   # 设置读取的字符足够大

print(lines)   # 输出读取到的文件内容
f.close()      # 关闭文件
