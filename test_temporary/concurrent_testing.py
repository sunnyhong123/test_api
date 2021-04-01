#coding=utf-8
import threading
from datetime import *
from test_temporary.test_register import register

#定义线程数
THREAD_NUM = 10
#定义循环次数
ONE_WORKER_NUM = 1

#需要进行并发测试的代码
def test():
    register()
    print("并发测试开始...")
    print(datetime.now())

def working():
    global ONE_WORKER_NUM
    for i in range(0,ONE_WORKER_NUM):
        test()

def thd():
    global THREAD_NUM
    Threads = []
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working(),name="T"+str(i))
        t.setDaemon(True)
        Threads.append(t)
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()
if __name__ == '__main__':
    thd()