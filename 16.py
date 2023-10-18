print("enter a number ")
no=int(input())
temp=no
p=0
while temp!=0:
	p=p+1
	temp=temp//10
temp=no
arm=0
while temp!=0:
	r=temp%10
	arm=arm+pow(r,p)
	temp=temp//10
if no==arm:
	print(no," is armstrong number")