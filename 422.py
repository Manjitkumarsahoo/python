#Read Only Parts of the File
#By default the read() method returns the whole text, but you can also specify how many characters you want to return:

f=open("data.csv","r")
print(f.read(8))
