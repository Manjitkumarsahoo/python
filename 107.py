#Find out sum of n natural numbeer using recursion

def sumofallno(n):
    if n==1:
        return n
    return n+sumofallno(n-1)

print(sumofallno(6))

