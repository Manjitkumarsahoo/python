#Regular expresion
#  findall()

"""  
[a-zA-Z0-9]- is a character class that 
matches any single character that is a 
lowercase letter (a to z), an uppercase
 letter (A to Z), or a digit (0 to 9).
"""
import re

txt = "I wA99nt To Be a Programmer"

x = re.findall("[a-zA-Z0-9]", txt)
print(x)