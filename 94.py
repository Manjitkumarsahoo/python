#Multi Threding
#How to change thred name

import threading
class Mythread(threading.Thread):
    def run(self):
        print("Hi",threading.current_thread().getName())

t=Mythread()
t.setName("sita")
t.start()

th=threading.current_thread()
th.setName("ram")
print("Bye",th.getName())

t.join()
