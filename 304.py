#Regular Expression
#  findall()            
"""
[]	A set of characters	"[A-M]"
Find all upper case characters alphabetically
 between "A" and "M":

"""

import re
txt=("I Want To Be a Programmer")
x=re.findall("[A-M]",txt)
print(x)
