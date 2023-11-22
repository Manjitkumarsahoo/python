#Regular expresion
#  findall()
#  \S=Returns a match where the string DOES NOT contain a white space character

import re
txt="i want to be a programmer "
x=re.findall("\S",txt)
print(x)
