#WAP take a string from keyword a swapcase

print("Enter a string")
s=input()
s1=""
for i in s:
    x=ord(i)
    if (x>=65 and x<=90) or (x>=97 and x<=122):
        if x>=97 and x<=122:
            s1=s1+chr(x-32)
        else:
            s1=s1+chr(x+32)
    else:
        s1=s1+chr(x)
print(s1)
