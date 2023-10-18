print("enter a number")
no=int(input())
temp=0
s=0
m=1
while no!=0:
    r=no%10
    s=s+r
    m=m*r
    no=no//10
if s==m:
    print("temp is a spy number")
