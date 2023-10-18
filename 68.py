#Parameter constructor in Parent and Child class

class A:
    def __init__(self,x):
        print("A class constructor",x)
class B(A):
    def __init__(self, x,y):
        super().__init__(x)
        print("B class constructor",y)
ob=B(10,20)
