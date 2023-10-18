#Differemt Type Of Variable

a=10                                            #global variable
class test:
    c=30
    def __init__(self,x,y):                      #x,y are formal or local variable
        z=40                                    #local variable
        self.x=x                                #self.x instance variable
        self.y=y                                #instance variable
b=20                                            #global variable
t=test(50,60)
t.z=70                                          #instance variable
print(t.x,t.y,t.z)