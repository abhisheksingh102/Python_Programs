# Python Read Files
f=open("abc.txt","r")
print(f.read())
print(f.read(5))
f.close()

# return one line by using the readline() method:
f=open("abc.txt","r")
print(f.readline())
print(f.readline())
f.close()

#By looping through the lines of the file, you can read the whole file, line by line
f=open("abc.txt","r")
for i in f:
    print(i)
f.close()

#-------------------------------------------------------------------------------------------------------------
# Python File Write

f=open("abc.txt","a")
f.write(" UP is a good state")
f.close()

f=open("abc.txt")
print(f.read())
f.close()

# The "w" method will overwrite the entire file
f=open("aks.txt","w")
f.write("He is from Ballia")
f.close()
f=open("aks.txt")
print(f.read())
f.close()

f=open("abc.txt","r")
print(f.readlines())
print(type(f))
f.close()

# Delete files

import os
if os.path.exists("abhi.txt"):
    os.remove("aks.txt")
else:
    print("The file doesn't exist")