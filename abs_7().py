# coding=gbk

# 绝对值在小游戏中的应用

import turtle
turtle.setup(600, 300)
turtle.screensize(500, 500, "green")
a = [+80, -40, +120, -70, -50, +130, -100]
turtle.shape('turtle')
turtle.speed(1)
turtle.pensize(4)
sum = 0
for num in a:
	turtle.forward(num)
	sum = sum + abs(num)

# 输出文字
printer = turtle.Turtle()
printer.write("小海龟爬行的总行程： " + str(num) + "\n\n", align = "right", font = ("楷体", 12, "bold"))
printer.write("小海龟得到的豆子数： " + str(num*3) + ' ', align = "right", font = ("楷体", 12, "bold"))
turtle.mainloop()

