#WAP count no of upper case using unicode

print("enter a string")
s=input()
up=0
for i in s:
    if ord (i)>=65 and ord(i)<=90:
        up=up+1
print("no of upper case=",up)
