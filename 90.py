#Inheritance in multithreding
#different task for multiple thread

import threading
class Mythread1(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hello")

class Mythread2(threading.Thread):
    def run(self):
        for i in range(5):
            print("Bye")

t1=Mythread1()
t2=Mythread2()

t1.start()
t2.start()

