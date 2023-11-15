#Sort element
#1st we convert tuple to list then sort and again convert to tuple

t=[10,40,20,70,55,77]
L=list(t)
L.sort()
t=tuple(L)
print(t)
