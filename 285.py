#Predefined function of Dict
#update()
#copy()

d={1:"A",2:"B",5:"C",4:10,2:"E"}
d.update({3:"u"})
print(d)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)


#copy
d1={1:"A",2:"B"}
d2=d1.copy()
d1.update({3:"C"})
print(d1)
print(d2)