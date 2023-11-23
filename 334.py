import re
txt = "8090519502"
x = re.findall("[7-9]\d\d\d\d\d\d\d\d\d", txt)

print(x)