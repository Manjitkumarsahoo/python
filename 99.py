#Synchronization in multi threding

import threading
def disp(name):
    for i in range(5):
        print("hello",name)

t1=threading.Thread(target=disp,args=("dhoni",))
t2=threading.Thread(target=disp,args=("virat",))

t1.start()
t2.start()

