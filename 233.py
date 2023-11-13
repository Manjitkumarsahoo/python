#Matrix add take input fron keybord and show transpoze Matrix

import sys
print("Enter 1st 2d array r and c")
r1=int(input())
c1=int(input())

if r1!=c1:
    print("squre matrix transpoze not possible")

L=[]
print("Enter 1st 2d matrix",r1*c1,"Element")
for i in range(r1):
    x=[]
    for j in range(c1):
        x.append(int(input()))
    L.append(x)

#display befor transpose

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j],end="\t")
    print()

#logic for transpose

for i in range(len(L)):
    for j in range(len(L[i])):
        if i<=j:
            temp=L[i][j]
            L[i][j]=L[j][i]
            L[j][i]=temp
    print()

#display after transpose

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j],end="\t")
    print()
    
