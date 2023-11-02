#find out the length of each words present in side a string
msg='Good morning to every one present here'
s=msg.split(' ')
data=list(map(lambda x:len(x),s))
print(data)
