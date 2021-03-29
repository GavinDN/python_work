# coding=gbk

# 动态刷新控制台输出

import time                                        # 导入时间模块
for i in range(10, -1, -1):
	time.sleep(1)                                  # 休眠1秒
	print("\r 距离结束还有 ".format(i), 'S', end='') # 输出内容到终端
