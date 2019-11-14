# Q. Write a Python Program to read first n lines of a file.

f=open('abc.txt','r')
n=int(input("Enter the number of line\n"))
for i in range(n):
    print(f.readline())
f.close()