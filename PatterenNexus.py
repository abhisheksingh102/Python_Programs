h=int(input())
w=int(input())

for i in range(w):
    print(' _ ',end=' ')

print()
for i in range(h*2):
    for j in range(w):
        if(i%2!=1 and j!=w-1):
            print("/ \\",end='_')
        elif(i%2==1):
            print("\\_/",end=' ')
        else:
            print("/ \\",end='')
    print()