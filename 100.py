#Synchronization ( using of acquire,release)

import time,threading
def disp(name):
    lock.acquire()
    for i in range(5):
        print("Hello",name)
        time.sleep(0.02)
    lock.release()

lock=threading.Lock()
t1=threading.Thread(target=disp,args=("Dhoni",))
t2=threading.Thread(target=disp,args=("Virat",))

t1.start()
t2.start()
