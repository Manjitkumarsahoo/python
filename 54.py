#CLASS PROGRAME

class test:
    def __init__(self,x,y):
        self.x=x
        self.y=y
print("enter two value")
t=test(int(input()),int(input()))
print(t.x,t.y)