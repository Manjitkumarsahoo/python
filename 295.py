c=0
for i in range(4,0,-1):
    for j in range(1,i+1,1):
        print(j,end="")
    for j in range(c):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    c=c+2
    print()
for i in range(1,5,1):
    for j in range(1,i+1,1):
        print(j,end="")
    for j in range(2*(4-i)):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    print()
    