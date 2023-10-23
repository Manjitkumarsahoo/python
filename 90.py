#Inheritance in multithreding
#different task for multiple thred

import threading
class Mythred1(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hello")

class Mythred2(threading.Thread):
    def run(self):
        for i in range(5):
            print("Bye")

t1=Mythred1()
t2=Mythred2()

t1.start()
t2.start()

