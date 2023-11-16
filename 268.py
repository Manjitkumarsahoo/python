#Remove element from a set
#using pop()

s={10,20,30,40,50}
s.pop()
print(s)


#another way
def Remove(s1):
    while s1:
        s1.pop()
        print(s1)

s1={10,20,30,40,50,60}
Remove(s1)

