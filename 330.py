#Split the string at the first white-space character:

import re
txt="Life is a journey. Enjoy the ride."
x=re.split("\s",txt,1)
print(x)
