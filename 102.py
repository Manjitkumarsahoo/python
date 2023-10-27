#Synchronization using semaphore

import threading
semaphore=threading.Semaphore(3)

def task(task_id):
    with semaphore:
        print(f"Task {task_id} is using the shared resource")
        for _ in range(3):
            pass

        print(f"Task{task_id} has finished")

threads=[]

for i in range(5):
    t=threading.Thread(target=task,args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print("All thread have completed")

