#Matrix add take input fron keybord and show upper trangle

import sys
print("Enter 1st  2d array r and c")
r1=int(input())
c1=int(input())

if r1!=c1:
    print("lower trangle not possible")

L=[]
print("Enter 1st 2d array",r1*c1,"element")
for i in range(r1):
    x=[]
    for j in range(c1):
        x.append(int(input()))
    L.append(x)

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j],end="\t")
    print()

for i in range(len(L)):
    for j in range(len(L[i])):
        if i>=j:
            print(L[i][j],end="\t")
        else:
            print(end="\t")
    print()

