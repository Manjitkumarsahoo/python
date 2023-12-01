import pandas

mydataset={
    'bikes':["bmw","ducati","tvs"],
    'passing':[5,3,2]
}

myvar=pandas.DataFrame(mydataset)

print(myvar)