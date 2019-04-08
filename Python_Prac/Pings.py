#!/usr/bin/python
#coding=utf-8
from threading import Thread
import subprocess
from Queue import Queue #插入队列的构造方法

num_threads = 16

ips=['10.42.0.146', '10.42.0.33', '10.42.0.35', '10.42.0.39', '10.42.0.31', '10.42.0.37', '10.42.0.29', '10.42.0.55', '10.42.0.41', '10.42.0.43', '10.42.0.45', '10.42.0.46', '10.42.0.47', '10.42.0.48', '10.42.0.44', '10.42.0.49'] #计划需要ping的地址

q = Queue()

def pingit(i, queue):
   while True:
      ip = queue.get()			#从队列中取出一个值
      print "thread %s is pinging %s" %(i, ip)
      ret = subprocess.call('ping -c 2 %s' %ip, shell=True, stdout=open('/dev/null','w')) #这里导致了，只能在linux下面的python用，正常则返回0,异常则返回1,通过是否正常返回来判断通断，stdout=('/dev/null', 'w')屏蔽ping的具体信息。这个是通了就是返回0,不通就是返回1.
      if ret != 0:
         print "%s is down\n" %ip
      else:
         print "%s is up\n" %ip
      queue.task_done()		#在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号

for i in range(num_threads):
   t = Thread(target=pingit, args=(i, q))
   t.setDaemon(True)
   t.start()
   for ip in ips:
      q.put(ip)
print "main thread is waiting ..."
q.join()	#Queue.joi()实际上意味着等队列为空，再执行别的操作
print "Done ..." 
