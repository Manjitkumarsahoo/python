#Change the thread name(another way)

import threading
def thread_function():
    threading.current_thread().name="NewThreadName"
    current_thread_name=threading.current_thread().name
    print(f"Current thred name:{current_thread_name}")


My_thread=threading.Thread(target=thread_function)

My_thread.start()

My_thread.name="CustomThredName"

thread_name=My_thread.name
print(f"Thread name:{thread_name}")
