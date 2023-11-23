import re
txt='Hello Everyone'

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x=re.findall("He..o",txt)
x1=re.findall("Ev.....e",txt)
print(x)
print(x1)
