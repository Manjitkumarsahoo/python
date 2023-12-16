#open the file and overwrite the cintent

f=open("demofile.txt","w")
f.write("Woops! i have deleted the content!")
f.close()

f=open("demofile.txt","r")
print(f.read())
