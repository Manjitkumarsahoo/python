#Constructor in inheritance

class A:
    def __init__(self):
        print("A class constructor")
class B(A):
    def __init__(self):

        #here we can call class A
        super().__init__();
        print("B class constructor")
ob=B()

