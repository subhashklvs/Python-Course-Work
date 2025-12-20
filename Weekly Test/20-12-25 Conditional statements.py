# Even or odd checker(if - else statement)
num=int(input("enter a number:"))
if num%2==0:
    print("even number")
else:
    print("odd numbers")
    
# Positive,Negative or zero(if-else -else)
num=int(input("enter a number:"))
if num>0:
    print("positive number")
elif num<0:
    print("Negative number")
else:
    print("zero")

# voting eligibility(simple if)
age=int(input("enter your age:"))
if age>=18:
    print("eligible to vote")
    
# largest of two numbers (if-else)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("The largest number is:", a)
else:
    print("The largest number is:", b)
    
    # or 
    
a=int(input())
b=int(input())
if a>b:
    print(a)
else:
    print(b)    
    
    
# largest of three numbers(nested if)
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
if n1>n2:
    if n1>n3:
        print(n1,"is the largest number")
    else:
        print(n3,"is the largest number")
else:
    if n2>n3:
        print(n2,"is the largest number")
    else:
        print(n3,"is the largest number")

    # or 

n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
if n1>n2 and n1>n3:
    print(n1,"is the largest number")
elif n2>n1 and n2>n3:
    print(n2,"is the largest number")
else:
    print(n3,"is the largest number")
    
    # or 
n1=int(input())
n2=int(input())
n3=int(input())
if n1>=n2 and n1>=n3:
    print(n1)
elif n2>n1 and n2>n3:
    print(n2)
else:
    print(n3)
    
# grade calculator(if-elif-else)
n=int(input("enter your marks:"))
if n>=90 
    print("a grade")
elif n>=80 and n<90:
    print("b grade")
elif n>=70 and n<80:
    print("c grade")
else:
    print("fail")
    
    
# login validation(nested if)
username=input("enter username:")
password=input("enter password:")
if username=="admin":
    if password=="1234":
        print("login successful")
    else:
        print("invalid password")
else:
    print("invalid username")
    
# number range checker(if-elif-else)
num=int(input("enter a number:"))
if num<0:
    print("negative number")
elif num<=100:
    print("number is in range 0-100")
else:
    print("number is out of range")
    
# simple calculator(if-elif-else)
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
operator=input("enter operator(+,-,*,/):")
if operator=="+":
    print(n1+n2)
elif operator=="-":
    print(n1-n2)
elif operator=="*":
    print(n1*n2)
elif operator=="/":
    print(n1/n2)
else:
    print("invalid operator")
    
# pass or fail checker(if-else)
n=int(input("enter your marks:"))
if n>=40:
    print("pass")
else:
    print("fail")
    


    