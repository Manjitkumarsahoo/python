#find prime number using function

def prime():
    print("enter a number ")
    no=int(input())
    c=True
    d=2
    if no==0 or no==1:
        c=False
    while d<=no//2:
        if no%d==0:
            c=False
            break
        d=d+1
    if c:
        print(no,"is prime number")
prime()