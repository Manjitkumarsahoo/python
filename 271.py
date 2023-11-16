#use intersection in set
#we also use ( & )

s1={10,20,30,40}
s2={30,70,40,90}

print(s1.intersection(s2))
print(s1&s2)

s1.intersection_update(s2)
print(s1)
print(s2)
