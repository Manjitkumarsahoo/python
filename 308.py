#Regular Expression
#  findall()  
#  [a-zA-Z]  -  find the charecter between "a" to "z" and "A" to "Z"

import re

txt = "I Want To Be a Programmer"

x = re.findall("[a-zA-Z]", txt)
print(x)