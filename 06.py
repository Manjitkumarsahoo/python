print("enter a number ")
no=int(input())
s=0
while no!=0:
	r=no%10
	s=s*10+r
	no=no//10
print("revno=",s)