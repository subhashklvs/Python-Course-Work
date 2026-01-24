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

# 2.Multilevel ingeritance: which a class is derived from another derived class, forming a chain of inheritance.

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

# 3. Multiple inheritance: single child class inherits properties and methods from more than one parent class.
# One child class → many parent classes

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
class Autoscroll:
    def scroll(self):
        print("now you can turn on the autoscroll")
class summarize:
    def summargizemsg(self):
        print("now the message can be summarized")
class InstagramV4(InstagramV3,Autoscroll,summarize):
    def repost(self):
        print("you can repost the post/reels")
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
print("venkata-InstagramV3")
venkata=InstagramV4()
venkata.post()
venkata.reel()
venkata.story()
venkata.restriction()
venkata.note()
venkata.highlights()

# 4. Hierarchical inheritance – multiple child classes inherit from a single parent class.
# one parent, multiple children

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
class Autoscroll:
    def scroll(self):
        print("now you can turn on the autoscroll")
class summarize:
    def summargizemsg(self):
        print("now the message can be summarized")
class summarizeV1(summarize):
    def algl(self):
        print("using Algo-1")
class summarizeV2(summarize):
    def art(self):
        print("Improving Art")
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
print("venkata-InstagramV3")
venkata=InstagramV3()
venkata.post()
venkata.reel()
venkata.story()
venkata.restriction()
venkata.note()
venkata.highlights()

# Hybrid Inheritance : combining two or more different types of inheritance (such as single, multiple, multilevel, or hierarchical) in a single program.
# It is a mix of inheritance types.

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
class Autoscroll:
    def scroll(self):
        print("now you can turn on the autoscroll")
class summarize:
    def summargizemsg(self):
        print("now the message can be summarized")
class summarizeV1(summarize):
    def algl(self):
        print("using Algo-1")
class summarizeV2(summarize):
    def art(self):
        print("Improving Art")
class InstagramV4(InstagramV3,Autoscroll,summarizeV1,summarizeV2):
    def repost(self):
        print("you can repost the post/reels")
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
print("venkata-InstagramV4")
venkata=InstagramV4()
venkata.post()
venkata.reel()
venkata.story()
venkata.restriction()
venkata.note()
venkata.highlights()
venkata.scroll()
venkata.summargizemsg()
venkata.repost()
venkata.algl()
venkata.art()

# Inheritance + Method Overriding :

class whatsapp():
    def status(self):
        print("upload a photo/video")
class whatsappV1(whatsapp):
    def status(self):
        print("upload a caption and emojis")
class whatsappV2(whatsapp,whatsappV1):
    def status(self):
        whatsapp.ststus(self)
        whatsappV1.status(self)
        print("like option and reactions are updated")
sai=whatsapp()
print("sai")
sai.status()
subhash=whatsappV1()
print("subhash")
subhash.status()
subhash=whatsappV2()
print("venkata")
subhash.status()