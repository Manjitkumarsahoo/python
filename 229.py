#Matrix add take input fron keybord

import sys
print("enter 1st 2d array r and c")
r1=int(input())
c1=int(input())

print("enter 2nd 2d array r and c")
r2=int(input())
c2=int(input())

if r1!=r2 or c1!=c2:
    print("addition not possible")
    sys.exit()

L1=[]
L2=[]
L3=[]
print("enter 1st 2d arrary",r1*c1,"elemnent")
for i in range(r1):
    x=[]
    for j in range(c1):
        x.append(int(input()))
    L1.append(x)

print("enter 2nd 2d array",r2*c2,"element")
for i in range(r1):
    x=[]
    for j in range(c2):
        x.append(int(input()))
    L2.append(x)

for i in range(len(L1)):
    x=[]
    for j in range(len(L1[i])):
        x.append(L1[i][j]+L2[i][j])
    L3.append(x)

print(L1)
print(L2)
print(L3)


