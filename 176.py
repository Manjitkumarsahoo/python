#WAP count no of char alp up lw vm co dg space sy word

print("enter a string")
s=input()
ch,al,up,lw,vw,co,dg,sp,sy,wd=0,0,0,0,0,0,0,0,0,0
for i in s:
    if i.isalpha():
        al=al+1
        if i.isupper():
            up=up+1
        else:
            lw=lw+1
        if i in "aeiouASEIOU":
            vw=vw+1
        else:
            co=co+1
    elif i.isdigit():
        dg=dg+1
    elif i.space():
        sp=sp+1
    else:
        sy=sy+1
    ch=ch+1
wd=sp+1

print("no of char=",ch)
print("no of alp=",al)
print("no of upper=",up)
print("no of lower=",lw)
print("no of vw=",vw)
print("no of co=",co)
print("no of digit=",dg)
print("no of space=",sp)
print("no of sy=",sy)
print("no of work=",wd)

