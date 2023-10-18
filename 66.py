#Constructur ,Inheritance ,Encapsulaion,Object instantiation

class person:
    def __init__(self,n,a):
        self.__name=n
        self.__age=a
    def setname(self,n):
        self.__name=n
    def setage(self,a):
        self.__age=a
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    
class student(person):
    def __init__(self, n, a, m):
        super().__init__(n, a)
        self.__mark=m

    def setmark(self,m):
        self.__mark=m

    def getmark(self):
        return self.__mark
    
s=student("manjit",25,99)
print("name=",s.getname())
print("age=",s.getage())
print("mark=",s.getmark())