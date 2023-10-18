print("enter a range")
rg=int(input())
for no in range(rg+1):
    temp=no
    s=0
    m=1
    while no!=0:
        r=no%10
        s=s+r
        m=m*r
        no=no//10
    if s==m:
        print(temp,"is a spy number")

