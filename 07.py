print("enter a number ")
no=int(input())
s=0
temp=no
while temp!=0:
	r=temp%10
	s=s*10+r
	temp=temp//10
if no==s:
	print(no ," is pd no")
else:
	print(no ," is not pd no")