#EXCEPTION HANDLE Index error

l=[10,20,30]
try:
    print(l[3])
except IndexError:
    print("index out of range")
print("program end")
