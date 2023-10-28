#Sum of a digits of a number using threding

import threading

input_ready=threading.Event()

input_value = None
sum_of_digit = 0

def input_thread():
    global input_value
    input_value = input("Enter a number: ")
    input_ready.set()

def sum_thread():
    input_ready.wait()
    global sum_of_digit
    for digit in str(input_value):
        sum_of_digit = sum_of_digit+int(digit)
    print(f"Sum of digit: {sum_of_digit}")

inputter=threading.Thread(target=input_thread)
summer=threading.Thread(target=sum_thread)

inputter.start()
summer.start()

inputter.join()
summer.join()