def fact(no):
    f=1
    while no>0:
        f=f*no
        no=no-1
    return f
print("enter a number")
no=int(input())
res=fact(no)
print("factorial=",res)
