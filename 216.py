#search and remove element
l=[19,18,17,16]
print("enter search element")
s=int(input())

for i in l:
    if i==s:
        l.remove(i)

print(l)
