#Regular expresion
#  findall()
"""
\w=	Returns a match where the string
 contains any word characters 
 (characters from a to Z, digits 
 from 0-9, and the underscore _ character)
"""

import re
txt="i want to be a programmer "
x=re.findall("\w",txt)
print(x)
