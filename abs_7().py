# coding=gbk

# ����ֵ��С��Ϸ�е�Ӧ��

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

# �������
printer = turtle.Turtle()
printer.write("С�������е����г̣� " + str(num) + "\n\n", align = "right", font = ("����", 12, "bold"))
printer.write("С����õ��Ķ������� " + str(num*3) + ' ', align = "right", font = ("����", 12, "bold"))
turtle.mainloop()
