#Nested dict

child1={"name":"muna","age":18}
child2={"name":"kuna","age":20}
child3={"name":"rita","age":23}
family={"c1":child1,"c2":child2,"c3":child3}
print(family)
print(family["c1"])
print(family["c2"]["age"])