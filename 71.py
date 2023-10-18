#Single inheritance

class A:
    def f1(self):
        print("f1 method")
class B(A):
    def f2(self):
        print("f2 method")
ob=B()
ob.f1()
ob.f2()
obj=A()
obj.f1()