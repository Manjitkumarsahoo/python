#Regular expresion
#  findall()

"""  
[^a-z][^A-Z][0-9]-not in range of
 a to z and also not in range of 
 A to Z but  in range of 0-9
"""
import re

txt = "I wA99nt To Be a Programmer"

x = re.findall("[^a-z][^A-Z][0-9]", txt)
print(x)