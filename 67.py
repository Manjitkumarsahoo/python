#Parameter constructor in Parent and Child class

class A:
    def show(self,x):
        print("show in parent",x)
class B(A):
    def show(self,x,y):
        super().show(x)
        print("show in child",y)
ob=B()
ob.show(10,20)