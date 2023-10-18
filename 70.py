#Constructor in inheritance

class A:
    def __init__(self):
        print("A class constructor")
class B(A):
    def __init__(self):
        print("B class constructor")
ob=B()
