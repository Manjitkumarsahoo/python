#odd matrix transpoze

import sys
print("enter 1st 2d array r and c")
r1=int(input())
c1=int(input())
#keyboad input
L=[]
print("enter 1st 2d array ",r1*c1," elements")
for i in range(r1):
	x=[]
	for j in range(c1):
		x.append(int(input()))
	L.append(x)


#dispaly
for i in range(0,len(L),1):
	for j in range(0,len(L[i]),1):
		print(L[i][j],end="\t")
	print()
L1=[]

#logic
for i in range(0,len(L[0]),1):
	x=[]
	for j in range(0,len(L),1):
		x.append(L[j][i])
	L1.append(x)
#dispaly
print("after transpoze")
for i in range(0,len(L1),1):
	for j in range(0,len(L1[i]),1):
		print(L1[i][j],end="\t")
	print()