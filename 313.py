#Regular expresion
#  findall()
#(" ")=find the no of space in the text

import re
txt="i want to be a programmer by 2023"
x=re.findall(" \d",txt)
print(x)