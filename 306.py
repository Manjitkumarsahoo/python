#Regular Expression
#  findall()            
"""
[]	A set of characters	"[0-9]"
find all the digit present in between "0" to "9"
"""

import re
txt=("I Want To Be a Programmer by 2023")
x=re.findall("[0-9]",txt)
print(x)
