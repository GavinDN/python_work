# coding=gbk

password = input("请输入您的密码（含英文）：").upper()  # 将输入的字符串转换为全部大写
name = input("请输入您的姓名（英文）：").capitalize()   # 将输入的字符串转换为首字母大写
school = input("请输入您的学校（英文）：").title()      # 将输入的单词全部转换为首字母大写
print(password, name, school)
