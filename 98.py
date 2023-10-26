#Multi Threding(calculate the time taken for exicution)

import time
def disp():
    for i in range(5):
        print("Hello")

def show():
    for i in range(5):
        print("Bye")

t=time.time()
disp()
show()
print("total time taken=",time.time()-t)

