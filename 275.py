#set comphersenion

s1={1,3,2,5,7}
s2={i*i for i in s1}
print(s2)

s3={i*i for i in s1 if i>2}
print(s3)


s4="Manjit"
s5={i for i in s4 if i in "aeiou"}
print(s5)
