#Herachial inheritance
class student:
    def __init__(self,n,r):
        self.__name=n
        self.__rollno=r
    def setname(self,n):
        self.__name=n
    def getname(self):
        return self.__name
    def setrollno(self,r):
        self.__rollno=r
    def getrollno(self):
        return self.__rollno

class enggstudent(student):
    def __init__(self,n,r,m):
        super().__init__(n,r)
        self.__Amark=m
    def setmark(self,m):
        self.__Amark=m
    def getmark(self):
        return self.__Amark

class midstudent(student):
    def __init__(self,n,r,m):
        super().__init__(n,r)
        self.__Bmark=m
    def setmark(self,m):
        self.__Bmark=m
    def getmark(self):
        return self.__Bmark


e=enggstudent("Manjit",1,99)
print("Name=",e.getname())
print("Rollno=",e.getrollno())
print("Mark=",e.getmark())

m=midstudent("Lulu",2,98)
print("Name=",m.getname())
print("Rollno=",m.getrollno())
print("Mark=",m.getmark())



