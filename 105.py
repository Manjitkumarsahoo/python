#calculate the squares, cubes, and factorial of a given number simultaneously  using multithreading

import threading
import math

def calculate_squares(number):
    squares = [num ** 2 for num in range(1, number + 1)]
    print("Squares:", squares)

def calculate_cubes(number):
    cubes = [num ** 3 for num in range(1, number + 1)]
    print("Cubes:", cubes)

def calculate_factorial(number):
    factorial = math.factorial(number)
    print("Factorial:", factorial)

number = int(input("Enter a number: "))

square_thread = threading.Thread(target=calculate_squares, args=(number,))
cube_thread = threading.Thread(target=calculate_cubes, args=(number,))
factorial_thread = threading.Thread(target=calculate_factorial, args=(number,))

square_thread.start()
cube_thread.start()
factorial_thread.start()

square_thread.join()
cube_thread.join()
factorial_thread.join()

print("Multithreading example completed!")
