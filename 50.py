#EXCEPTION HANDLE KeyError

d={1:"A",3:"B"}
try:
    print(d[4])
except KeyError:
    print("key not found")
print("programe end")
