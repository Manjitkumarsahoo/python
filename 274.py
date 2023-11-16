#is subset()
#is superset()
#is disjoint()

s1={2,9}
print(s1.issubset({2,5,7,9}))
print(s1.issuperset({2,9}))


s2={3,0}
s3={2,7}
print(s2.isdisjoint(s3))
