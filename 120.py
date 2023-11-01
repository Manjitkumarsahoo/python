#Filter all the negative value from an sequence using filter

l=[10,20,-34,-56.77,-89]
data=list(filter(lambda x:x<0,l))
print(data)
