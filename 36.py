#find gcd using function

def gcd(a,b):
    while b!=0:
        a,b=b,a %b
    return a
num1=23
num2=43

result=gcd(num1,num2)
print(f"The gcd od{num1} and {num2} is {result}")