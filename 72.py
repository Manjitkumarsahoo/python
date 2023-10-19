# Multilevel inheritance
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
    def __init__(self,n,a,m):
        super().__init__(n,a)
        self.__mark=m
    def setmark(self,m):
        self.__mark=m
    def getmark(self):
        return self.__mark
class mca(student):
    def __init__(self,n,a,m,r):
        super().__init__(n,a,m)
        self.__rollno=r
    def setrollno(self,r):
        self.__rollno=r
    def getrollno(self):
        return self.__rollno
s=mca("manjit",25,98,1)
print("name=",s.getname())
print("age=",s.getage())
print("rollno=",s.getrollno())
print("mark=",s.getmark())

m=mca("lulu",24,99,1)
print("name=",m.getname())
print("age=",m.getage())
print("rollno=",m.getrollno())
print("mark=",m.getmark())

    