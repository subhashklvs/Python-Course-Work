# 1.print numbers from 1 to n in a single line separated by space :

n=int(input("enter a number: "))
for i in range(1,n+1):
    print(i,end=" ")
    
# 2.Rigth Angle number triangle :

rows = int(input("enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 3.Inverted Star Pattern :

rows = int(input("enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# 4.Multiplication Table :

n = int(input("enter a number: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} x {j} = {i*j}")
    print()

# 5.pyramid star  Pattern :

rows = int(input("enter number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# 6.List Comprehensions - Even Numbers :

n=int(input("enter a number: "))
even_numbers=[i for i in range(1,n+1) if i%2==0]
print(even_numbers) 

# 7.List Comprehensions - Square odd Numbers :

n=int(input("enter a number: "))
odd_squares=[i**2 for i in range(1,n+1) if i%2!=0]
print(odd_squares)

# 8.Tought-conditional pattern(Nested loops) :

n=int(input("enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("1",end=" ")
        else:
            print("*",end=" ")
    print()

# 9.List Comprehension – Word Filter :

words=input().split()
filtered_words=[word for word in words if len(word)>3]
print(filtered_words)

# 10.Floyd’s Triangle :

n=int(input("enter a number: "))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()