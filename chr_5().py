# coding=gbk

# 自动生成单个随机字母（a~z）

import random             # 导入random模块
a=random.randint(65, 123) # 生成65~123之间的随机数
# 将a表示的ASCII码使用的chr()函数转换为对应的字母
a1=chr(a)
print(a1)                 # 输出：y
