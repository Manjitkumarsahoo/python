#Regular expresion
#  findall()
#  wan\B  -- found if wan can present start of a word in the text


import re
txt="I want to be a programmer"
x=re.findall(r"wan\B",txt)
print(x)

if x:
    print("match found")
else:
    print("match not found")
