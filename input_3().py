# coding=gbk
sum = 0
for x in input("请输入多个加数，中间用空格分隔：").split(" "):
	sum = sum+int(x)
print(sum)
