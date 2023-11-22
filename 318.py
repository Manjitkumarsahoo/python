#Regular expresion
#  findall()
"""
\W=	Returns a match where the 
string DOES NOT contain any word 
characters

"""

import re
txt="i want to be a programmer "
x=re.findall("\W",txt)
print(x)
