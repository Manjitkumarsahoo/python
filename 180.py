#WAP take string from keyboad and cinvert to upper case lower case

print("Enter a string")
s=input()
s1=""
for i in s:
    x=ord(i)
    if x>=65 and x<=97:
        s1=s1+chr((x+32))
    else:
        s1=s1+chr(x)
    print(s1)
    