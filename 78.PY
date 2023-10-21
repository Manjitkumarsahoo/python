#Addition operator overloding

class Employee:
    def __init__(self,sal):
        self.sal=sal
    def __add__(self,other):
        return self.sal+other.pkt_money
class student:
        def __init__(self,pkt_money):
            self.pkt_money=pkt_money
        
e=Employee(10000)
s=student(5000)
print(e+s)
