#Inheritance in multithreading
#Multithred same class

import threading
class Mythread(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hello")

t=Mythread()
t.start()

t1=Mythread()
t1.start()
