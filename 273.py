#use of symmetric in symmetric_difference
#we can also use (^)

s1={11,22,33,44,55}
s2={66,55,77,88,11}

print(s1.symmetric_difference(s2))
print(s1^s2)

s1.symmetric_difference_update(s2)
print(s1)
print(s2)