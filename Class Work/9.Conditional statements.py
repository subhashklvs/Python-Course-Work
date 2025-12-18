# Conditional statements :
# execites a block of code if a specified condition is true.
# if condition :  

# 1. simple if statement :  code to be executed if condition is true

age = 20
if age >= 18:
    print("Eligible to vote")

# 2. if-else statement : code to be executed if condition is true, else code to be executed if condition is false

num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. if-elif-else statement : code to be executed if first condition is true, else if second condition is true, else code to be executed if both conditions are false

age= 100
if age<= 90:
    print("Eligible for vote")    
elif age<= 200:
    print("Eligible foe driving license")
else:
    print("Eligible for marriage")
    
# 4. nested if statement : an if statement inside another if statement

num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
        



 