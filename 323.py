import re
txt="Hello Everyone"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "e":
x=re.findall("He.*e",txt)
print(x)