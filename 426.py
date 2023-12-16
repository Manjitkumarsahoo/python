#Write to an Existing File
#To write to an existing file, you must add a parameter to the open() function:

#"a" - Append - will append to the end of the file

#"w" - Write - will overwrite any existing content
f=open("demofile.txt","a")

f.write("I am from BBSR")
f.close()

f=open("demofile.txt","r")

print(f.read())

