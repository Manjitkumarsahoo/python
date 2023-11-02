#find out square of each number present inside tuple using map()
t=(3,5,7,4,8,7)
data=list(map(lambda x:x*x,t))
print(data)