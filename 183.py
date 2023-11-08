#WAP take string from keyword every word first letter must be capital

print("Enter a string")
s=input()
s1=""
for i in range(len(s)):
    x=ord(s[i])
    s1=s1+chr(x)
    if x==32:
        s1=s1+chr(ord(s[i+1])-32)

print(s1)

