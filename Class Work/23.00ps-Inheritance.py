# What is Inheritance?
# Inheritance = One class acquires properties and methods of another class.
# 👉 Parent class → Base / Super class
# 👉 Child class → Derived / Sub class
# Real-life example 👨‍👦
# Parent: Father (house, land)
# Child: Son (inherits father’s property) 
# Same concept in Python 🐍
#🔹 Why do we need Inheritance?
#✔ Code reusability
#✔ Less duplication
#✔ Easy maintenance
#✔ Supports real-world relationships

#1. single inheritance : Single inheritance is a type of inheritance in which a child class inherits from only one parent class

class InstagramV1:
    def post(self):
        print("you can post your images")
    def reel(self):
        print("you can upload your videos")
        
class InstagramV2(InstagramV1):
    def story(self):
        print("you can upload the 24 hrs story")
    def restriction(self):
        print("you can restrict the account")
print("subhash-InstagramV2")
subhash=InstagramV1()
subhash.post()
subhash.reel()
print("sai-InstagramV2")
sai=InstagramV2()
sai.post()
sai.reel()
sai.story()
sai.restriction()

# 2.Multilevel: which a class is derived from another derived class, forming a chain of inheritance.

class InstagramV1:
    def post(self):
        print("you can post your images")
    def reel(self):
        print("you can upload your videos")
class InstagramV2(InstagramV1):
    def story(self):
        print("you can upload the 24 hrs story")
    def restriction(self):
        print("you can restrict the account") 
class InstagramV3(InstagramV2):
    def note(self):
        print("you can add the not")
    def highlights(self):
        print("you can restrict the account")
print("subhash-InstagramV2")
subhash=InstagramV1()
subhash.post()
subhash.reel()
print("sai-InstagramV2")
sai=InstagramV2()
sai.post()
sai.reel()
sai.story()
sai.restriction()
print("venkata-InstagramV3")
venkata=InstagramV3()
venkata.post()
venkata.reel()
venkata.story()
venkata.restriction()
venkata.note()
venkata.highlights()
