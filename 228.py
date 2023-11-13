#keybord input add display element of list

print("enter 1st list data")
L1=eval(input())

print("Enter 2nd list data")
L2=eval(input())

L3=[]

for i in range(len(L1)):
    x=[]
    for j in range(len(L1[i])):
        x.append(L1[i][j]+L2[i][j])
    L3.append(x)

print(L3)
