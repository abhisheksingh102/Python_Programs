# Q. Write a python program to read last n lines of a file.

f=open('abc.txt','r')
n=int(input("Enter the no of last n line to be readed\n"))
l=f.readlines()
c=len(l)
f.seek(0)
for i in range(c-n):
    f.readline()
for i in range (n):
    print(f.readline())
f.close()