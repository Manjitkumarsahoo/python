class Student:
    def __init__(self, n, r, m, s):
        self.__name = n
        self.__rollno = r
        self.mark = m
        super().__init__(s)

    def setRollno(self, r):
        self.__rollno = r 

    def getRollno(self):
        return self.__rollno

    def setName(self, n):
        self.__name = n 

    def getName(self):
        return self.__name

    def setMark(self, mark):
        self.mark = mark

    def getMark(self):
        return self.mark

class Sports:
    def __init__(self, m):
        self.Smark = m

class Result(Student, Sports):
    def __init__(self, n, r, m, s):
        super().__init__(n, r, m, s)
        self.Smark = s  

re = Result("muna", 1, 90, 85)  
print("name =", re.getName())
print("rollno =", re.getRollno())
print("mark =", re.getMark())
print("sports mark =", re.Smark)
