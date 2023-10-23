#Inheritance in multithreading
#Multithred same class

import threading
class Mythred(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hello")

t=Mythred()
t.start()

t1=Mythred()
t1.start()
