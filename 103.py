#Thread communication using queues mudule

import threading
import queue
import time

message_queue=queue.Queue()

def sender_thread():
    messages=["I","Love","Riding"]
    for message in messages:
        message_queue.put(message)
        print(f"sent:{message}")
        time.sleep(1)

def reciver_thread():
    while True:
        message=message_queue.get()
        print(f"Received:{message}")
        message_queue.task_done()

sender=threading.Thread(target=sender_thread)
receiver=threading.Thread(target=reciver_thread)

sender.start()
receiver.start()

sender.join()
time.sleep(5)


