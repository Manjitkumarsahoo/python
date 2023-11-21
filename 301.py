#Regular Expression
"""
^	Starts with	"^hello"	
$	Ends with   "planet$"

"""


import re
txt="I love Riding"
x=re.search("^I.*Riding$",txt)

if x:
    print("match found")
else:
    print("not found")
