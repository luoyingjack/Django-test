# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/25 下午4:13' 

import os
import time

print("在创建子进程之前，进程信息 pid=%s, ppid=%s" % (os.getpid(), os.getppid()))

pid = os.fork()

if pid == 0: #子进程分支
	print("子进程信息：返回值：%s, pid=%s, ppid=%s" % (pid, os.getpid(), os.getppid()))
	time.sleep(1)
else:
	print("父进程信息：返回值:%s,  pid=%s, ppid=%s" % (pid, os.getpid(), os.getppid()))
	time.sleep(1)
	pid, result = os.wait()
	print("回收完后，进程信息：返回值：%s, result=%s" % (pid, result))


print("fork创建完后: pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
