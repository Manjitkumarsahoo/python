#WAP take string from keybord every word must first letter must capital

print("enter a string")
s=input()
s1=""
i=1
s1=s1+chr(ord(s[0])-32)
while i<=len(s)-1:
    x=ord(s[i])
    s1=s1+chr(x)
    if x==32:
        s1=s1+chr(ord(s[i+1])-32)
        i=i+1
    i=i+1
print(s1)
