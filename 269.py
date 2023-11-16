#Remove element from a set
#using discard()

s={11,22,33,44,55,66,77}

while s:
    s.discard(max(s))
    print(s)

    