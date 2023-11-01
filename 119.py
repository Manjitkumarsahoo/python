#write a program to filter all the even value from a list using lambda
l=[3,23,54,77,984,76,75,88]
data=list(filter(lambda x:x%2!=0 ,l))
print(data)
