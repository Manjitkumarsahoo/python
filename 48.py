#EXCEPTION HANDLE USING except BaseException

print("A")
try:
    print("try start")
    print("10//0")
    print("try end")
except BaseException:
    print("exception handle all type")
print("program end")
