#add data of two list using lambda function
l1=[10,20,30,40,50]
l2=[11,22,33,44,55]

data=list(map(lambda x,y:x+y,l1,l2))

print(data)

