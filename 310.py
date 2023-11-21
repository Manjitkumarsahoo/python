#Regular Expression
#  findall()
"""  
[a-z][A-Z][0-9]  -  find the three word charecter
 which start with lower latter and 
middle one is upper latter and end between 0 to 9
"""

import re

txt = "I wA9nt To Be a Programmer"

x = re.findall("[a-z][A-Z][0-9]", txt)
print(x)