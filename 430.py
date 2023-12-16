#Check if File exist:
#To avoid getting an error, you might want to check if the file exists before you try to delete it:


import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("This file does not exist")