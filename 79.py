#Lessthan operator overloading

class Lessthan:
    def __init__(self,m,s):
        self.m=m
        self.s=s
    def show(self):
        print(self.m,"+" ,self.s, "i")
    def  __lt__(self,c2):
        if self.m<c2.m and self.s<c2.s:
            return True
        else :
            return False
        
c1=Lessthan(4,2)
c2=Lessthan(8,4)
print(c1 < c2)