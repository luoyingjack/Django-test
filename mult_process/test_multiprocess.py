# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/25 下午4:29' 
import os
from multiprocessing import Process, Pool
import time

def myfunc(name):
	print(f"执行myfunc进程：{os.getpid()}")
	print("hello" + name)


def test_multiprocess():
	print(f"主进程信息：{os.getpid()}")
	ps = Process(target=myfunc, args=('hujingtao',))
	print("#####启动前####")
	print(ps.is_alive())
	print(f"ps 进程信息{ps.ident}")
	ps.start()
	print("#####启动后####")
	print(ps.is_alive())
	print(f"ps 子进程信息{ps.ident}, 主进程{os.getpid()}")

	ps.join()
	ps.terminate()
	print(ps.is_alive())
	print(f"ps 子进程信息{ps.ident}, 主进程{os.getpid()}")


def work(msg):
	time.sleep(0.01)
	return msg

def test_multiprocess_pool():
	begin_time = time.time()
	pool = Pool(processes=10)
	for i in range(1000):
		msg = "work-%s" % i
		pool.apply_async(work, args=(msg, ))

	pool.close()
	pool.join()
	end_time = time.time()
	use_time = int(end_time - begin_time)
	print(f"test_multiprocess_pool, all work has done. use_time:{use_time}")


def test_loop():
	begin_time = time.time()
	for i in range(1000):
		msg = "work-%s" % i
		work(msg)
	end_time = time.time()
	use_time = int(end_time - begin_time)
	print(f"test_loop, all work has done. use_time:{use_time}")


if __name__ == "__main__":

	test_multiprocess_pool()
	print("##########################")
	test_loop()

