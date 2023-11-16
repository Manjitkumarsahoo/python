#Use Differnce in set
#we can also use (-)

s1={10,20,30,40}
s2={40,60,70,80,30}

print(s1.difference(s2))
print(s1-s2)


s1.difference_update(s2)
print(s1)
print(s2)
