#Non-tail Recursion

def fun(num):
    if num==4:
        return
    else:
        fun(num+1)
        print(num)
fun(0)

        
