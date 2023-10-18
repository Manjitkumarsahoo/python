#find gcd and  functionlcm using

def gcdlcm():
    print("enter two nos")
    no1=int(input())
    no2=int(input())
    if no1>=no2:
        n=no1
        d=no2                 
    else:                      
        n=no2                 
        d=no1                 
    r=n%d
    while r!=0:
        n=d
        d=r
        r=n%d
    print("gcd=",d)
    print("lcm=",no1*no2//d)
gcdlcm()