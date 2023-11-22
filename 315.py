#Regular expresion
#  findall()
#  \s=Returns a match where the string contains a white space character

import re
txt="i want to be a programmer "
x=re.findall("\s",txt)
print(x)
