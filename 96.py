
import threading
class MyThread1(threading.Thread):
    def run(self):
        
        for i in range(5):
            print(threading.current_thread().name,"hello")
th=threading.current_thread()
t1=MyThread1()
t2=MyThread1()
th.name="main change"
t1.name="ram"
t2.name="sita"
print(threading.current_thread().name)
t1.start()
t2.start()
