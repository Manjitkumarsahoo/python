#Replace all white-space characters with the digit "9":

import re
txt="Life is a journey. Enjoy the ride."
x=re.sub("\s","9",txt)
print(x)
