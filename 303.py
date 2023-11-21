#Regular Expression
#  findall()            
"""
[]	A set of characters	"[a-m]"
Find all lower case characters alphabetically 
not in between "a" and "m":

"""

import re
txt=("i want to be a programmer")
x=re.findall("[^a-m]",txt)
print(x)
