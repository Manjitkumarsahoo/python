#key/value object as series

import pandas as pd

calories={"day1":420,"day2":380,"day3":869}

x=pd.Series(calories)

print(x)
