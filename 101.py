#Multi Threding using acquire  and release

import threading,time
class Mythread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        lock.acquire()
        for i in range(5):
            print("Hello",self.name)
            time.sleep(0.02)
        lock.release()

lock=threading.Lock()
t1=Mythread("Manjit")
t2=Mythread("Lulu")

t1.start()
t2.start()
