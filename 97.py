#Multi Threding (use of join(),sleep())

import time,threading
def disp():
    for i in range(5):
        print("Hello")
        time.sleep(0.02)

def show():
    for i in range(5):
        print("Bye")
        time.sleep(0.03)

t1=threading.Thread(target=disp)
t2=threading.Thread(target=show)
t1.start()
t2.start()
t1.join()
t2.join()

for i in range(5):
    print("main ok")
    
