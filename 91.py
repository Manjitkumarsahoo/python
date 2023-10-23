#Inheritance in multithreding
#Single task multiple thred

import threading
class Mythred1(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hello")

t1=Mythred1()
t2=Mythred1()

t1.start()
t2.start()
