def fact():
    print("enter a number")
    no=int(input())
    fact=1
    while no>0:
        fact=fact*no
        no=no-1
    print("factorial=",fact)
fact()
    