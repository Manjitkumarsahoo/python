#write a program to filter all the even value from a list using lambda

l=[10,20,32,13,12,89,19]
data=list(filter(lambda x:x%2==0,l))
print(data)

