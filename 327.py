import re
txt="Life is a journey. Enjoy the ride."

#Check if the string contains either "Life" or "ride":

x=re.findall("Life|ride",txt)
print(x)
if x:
    print("Yes there is at least one match")
else:
    print("No match")


