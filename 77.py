#Operator overloading

class Mycomplex:
    def __init__(self,r,i):
        self.__r=r
        self.__i=i
    def show(self):
        print(self.__r,"+",self.__i,"i")
    def __add__(self,c2):
        c3=Mycomplex(0,0)
        c3.__r=self.__r+c2.__r
        c3.__i=self.__i+c2.__i
        return c3
c1=Mycomplex(2,3)
c2=Mycomplex(3,4)
c3=c1+c2
c1.show()
c2.show()
c3.show()
