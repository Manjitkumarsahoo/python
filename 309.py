#Regular Expression
#  findall()
"""  
[a-z][A-Z]  -  find the two word charecter
 which start with lower latter and 
end with upper latter
"""

import re

txt = "I wAnt To Be a Programmer"

x = re.findall("[a-z][A-Z]", txt)
print(x)