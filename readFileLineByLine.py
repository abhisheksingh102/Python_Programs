# Q. Write a python program to read file line by line and store it into a list.

f=open('abc.txt','r')
n=f.readlines()
print(n)
for i in (n):
    print(i)
f.close()