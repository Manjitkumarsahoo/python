#Regular expresion
#  findall()
# mer\b  -- found matchn if 'mer' can present in the end of text
import re
txt="I want to be a programmer"

x=re.findall(r"mer\b",txt)
print(x)

if x:
    print("match found")
else:
    print("match not found")