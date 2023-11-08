#WAP count no of lower case

print("Enter a string")
s=input()
lw=0
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        lw=lw+1
print("no of lower case=",lw)