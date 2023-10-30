#Another star pattern using recurtion
def star(num):
    print("*"*num)
    if num==1:
        return
    star(num-1)

star(5)