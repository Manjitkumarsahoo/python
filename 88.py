# Inheritance using thread class 

import threading
class Mythread(threading.Thread):
    def run(self):
        for i in range(5):
             print("Hello")

t=Mythread()
t.start()
for i in range (5):
    print("Bye")