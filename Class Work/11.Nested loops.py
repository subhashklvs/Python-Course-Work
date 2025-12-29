# Nested loops : 

for i in range(5):
    for j in range(5):
        print('*',end='')
    print()

for i in range(4):
    for j in range(5):
        print(j+1,end=' ')
    print()
    
for i in range(5):
    for j in range(6):
        print(i+1,end=' ')
    print()
   
# Left Side Pyramid  
rows=int(input("enter the size:"))
for i in range(1,rows+1):
    for j in range(i):
        print('*',end=" ")
    print()
   
# Reverse 
n=int(input("enter the size:"))
for i in range(n):
    for j in range(n-i):
        print("*",end=' ')
    print() 
    
# right side pyramid

n=int(input("enter the size:"))
for i in range(n):
    for space in range(n-1-i):
        print(" ",end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()

# Reverse

n=int(input("enter the size:"))
for i in range(n):
    for space in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print('*',end=" ")
    print()
    
# Hollow rectangle pattern
n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
    
# Z pattern 
n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()

# X patternms
n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()