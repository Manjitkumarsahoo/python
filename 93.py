#Multi Threding 
#Hoe to know current thred name (another way)

import threading
class Mythread(threading.Thread):
    def run(self):
        print("Hi",threading.current_thread().getName())

t=Mythread()
t.start()
print("Bye",threading.current_thread().getName())
