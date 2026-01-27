# polymorphism : Polymorphism allows same function or method name to perform different tasks.
# Types: Function polymorphism, Method overriding, Operator overloading, Duck typing

# 1. Methof Overriding : a child class provides its own implementation of a method that is already defined in the parent class.
# Key Rules :
# 1.Method name must be same
# 2.Parameters must be same
# 3.Happens in inheritance
# 4.Child method overrides parent method

class Hotstar:
    def __init__(self,name):
        self.name=name
        print(f"\nHey{self,name}!\nWelcome to the Hotstar")
    def playvideo(self):
        print("Ads will run")
        print("limited access for videos")
        print("limited quality")
        print("speed is limited upto 2x")
        print("background run is not pos1sible")
    def login(self):
        print("limited logins")
    def search(self):
        print("you can search")
    def menu(self):
        print("you can see the menu card")
    def addtofav(self):
        print("you can add movies to the fav list")
class premiumHotstar(Hotstar):
    def __init__(self,name):
        self.name=name
        print(f"Hey{self,name}!\nWelcome to the Hotstar")
    def playvideo(self):
        print("Ads will not run ")
        print("full access for all the videos")
        print("high quality")
        print("speed is upto 4x")
        print("background run is possible")
    def login(self):
        print("multiple logins")
subhash=premiumHotstar('subhash')
subhash.playvideo()
subhash.login()
subhash.search()
subhash.addtofav()
subhash.menu()
sai=Hotstar('sai')
sai.playvideo()
sai.login()
sai.search()
sai.addtofav()
sai.menu()

# operator overloading : Same operator behaves differently for different objects.
# Operator overloading is a type of polymorphism that allows operators to perform different operations depending on the operands using special methods in Python.
# Operator + Special Method = Operator Overloading.
class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return self.num+other.num
    def __sub__(self,other):
        return self.num-other.num
    def __mul__(self,other):
        return self.num*other.num
    def __floordiv__(self,other):
        return self.num//other.num
    def __gt__(self,other):
        return self.num>other.num
    def __lt__(self,other):
        return self.num<other.num
    def __eq__(self,other):
        return self.num==other.num
    def __str__(self):
        return str(self.num)
n1=Number(20)
n2=Number(10)
print(n1+n2)
print(n1-n1)
print(n1*n2)
print(n1//n2)
print(n1>n2)
print(n1<n2)
print(n1==n2)