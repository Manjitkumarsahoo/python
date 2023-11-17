#Remove item from dict
#pop()
#popitem()

d={1:"A",2:"B",5:"C",4:10,2:"E"}
d.pop(2)
print(d)


d1={1:"A",2:"B",5:"C",4:10,2:"E"}
d1.popitem()
print(d1)


d2={1:"A",2:"B",5:"C",4:10,2:"E"}
d2.clear()
print(d2)