# class: A class is a blueprint or template to create objects.
# It contains variables (data) and methods (functions).

#1. declaring a class:"
# class Student:
    # stmts 
    
# 2. Write a Python program to demonstrate class variables using an Instagram class.

class instagram:
    settings=['visi','priv','....']
    pass
subhash=instagram()
venkata=instagram()

# 3. Design a class to represent a Flipkart user and print user information using a class method.

class Filpkart:
    def userinfo(self,name,password,mobileno):
        self.name=name
        self.password=password
        self.mobileno=mobileno
        print(f"userinfo:\nName:{self.name}\npassword:{self.password}\nmobile no:{self.mobileno}")
subhash=Filpkart()
subhash.userinfo("sai123","sai@123",9876543213)

# Using Construction :

class Amazon:
    def __init__(self, name, password, mobileno):
        self.name = name
        self.password = password
        self.mobileno = mobileno
    def userinfo(self):
        print(f"User Info:\nName: {self.name}\nPassword: {self.password}\nMobile No: {self.mobileno}")
subhash = Amazon("sai123", "sai@123", 9876543213)
subhash.userinfo()

