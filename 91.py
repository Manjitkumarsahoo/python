#Inheritance in multithreding
#Single task multiple thread

import threading
class Mythread1(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hello")

t1=Mythread1()
t2=Mythread1()

t1.start()
t2.start()
