#Add multiple element in set
#using list comprehension

s={10,20,30}
s=list(s)

L=[40,50,60]

s+=[i for i in L if i not in s]

print(s)

