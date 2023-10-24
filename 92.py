#Multi Threading
# how to know current thred name 

import threading
class Mythread(threading.Thread):
    def run(self):
        print("Hi",threading.current_thread())

t=Mythread()
t.start()
