#EXCEPTION HANDLE USING except Exception

print("A")
try:
    print("try start")
    print(10//0)
    print("try end")
except Exception:
    print("exception hamdle all type")
print("end program")