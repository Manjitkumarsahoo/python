#Tail Recursion
def fun(num):
    if num==4:
        return
    else :
        print(num)
        fun(num+1)

fun(1)