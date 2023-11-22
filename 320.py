#Regular expresion
#  findall()

import re
txt="I want to be a programmer"
x=re.findall(r"\Bmer",txt)
print(x)

if x:
    print("match found")
else:
    print("match not found")
