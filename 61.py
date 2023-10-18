#Setter and Getter

class Student:
    def __init__(self,n,r,m):
        self.__name=n
        self.__rollno=r
        self.__mark=m
    def setName(self,n):
        self.__name=n
    def setRollno(self,r):
        self.__rollno=r
    def setMark(self,m):
        self.__mark=m
    def getName(self):
        return self.__name
    def getRollno(self):
        return self.__rollno
    def getMark (self):
        return self.__mark
    def update(self,n,r,m):
        self.__name=n
        self.__rollno=r
        self.__mark=m
    def show(self):
        print("name=",self.__name)
        print("rollno=",self.__rollno)
        print("mark=",self.__mark)
s=Student("muna",1,98)
s.show()
s.setName("muna das")
print("name=",s.getName())
s1=Student("kuna",2,35)
s1.update("gita",3,45)
s1.show()