#filter out all the common element from both list using filter() function

a=[10,20,30,40,50]
l=[40,50,60,70,80]

data=list(filter(lambda x:x in a,l))

print(data)
