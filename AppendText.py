# Q. Write a program to append and display file.

f=open('abc.txt','a+')
f.write('\nabhi')
f.close()
f=open('abc.txt','r')
print(f.read())
f.close()