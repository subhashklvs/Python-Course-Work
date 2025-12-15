#1. Convert the string to lowerCase
text="Hello World"
c=text.lower()
print(c)

#2. Convert the String to the upper case

greetings="good morning"
c=greetings.upper()
print(c)

#3.Remove Leading and Tralling Spaces

data=" python "
c=data.strip()
print(c)

#4.  Replace "tough with easy"

line="Python is tough"
c=line.replace("tough","easy")
print(c)

#5.Count how many times of a appears
word="banana"
c=word.count("a")
print(c)

#6. Split the string into a list of words
text="python is fun"
c=text.split()
print(c)

#7. Find the Length of the String
s="learn python"
c=len(s)
print(c)

#8.Chech Whether the string is alphanumeric

value="test123"
c=value.isalnum()
print(c)

#9. Convert to LowerCase and Captilize the First Letter

t="HELLO"
c=t.lower()
d=c.capitalize()
print(d)

#10.  Check if the string ends with.com

email="studentgmail.com"
c=email.endswith(".com")
print(c)

#11.  Sort the List in ascending order

n=[45,67,89,32]
c=n.sort()
print(n)

#12.Add the 40 to the end of the list

n=[10,20,30]
c=n.append(40)
print(n)

#13.Remove the "blue" element in the list

c=["red","blue","green"]
ca=c.pop(1)
print(ca)

#14.count the how many times 2 appears

values=[1,2,3,2,4,5]
c=values.count(2)
print(c)

#15. join items into a single string seperated by commas

i = ["pen", "book", "pencil"]
result = ",".join(i)
print(result)

#16.Reverse the List

s=[100,90,80]
c=s[::-1]
print(c)

#17.Get Second Element

s=("Anu","Ravi","Meena")
c=s[1]
print(c)

#18.convert the tuple into the list

d=("id101","sita","CSE")
c=list(d)
print(c)

#19.find the Maximum element

d=(5,3,9,1)
c=max(d)
print(c)

#20.Get the last 2 elements using Slicing

g = ("a", "b", "c", "d")
result = g[-2:]
print(result)

#21.convert both to integers and find sum

a="10"
b="20"
c=int(a)
d=int(b)
e=c+d
print(e)

#22.convert the number into the String

n=35
c=str(n)
print(c)

#23.Find the remaindder when x divided by y

x=10
y=3
c=x%y
print(c)

#24.find the raised to the power b

a=5
b=2
c=a**b
print(c)

#25.check whether p is less than q

p=15
q=20
c=p<q
print(c)

#26.Find the sum of all elements

n=[1,2,3,4,5]
c=sum(n)
print(c)

#27.  find the maximum element

d=[1,3,7,9]
c=max(d)
print(c)

#28.  count the number of occurrences of "s"

word="mississippi"
c=word.count("s")
print(c)

#29.  replace "love" with "learn"

text="i love pytthon"
c=text.replace("love","learn")
print(c)

#30.convert list into tuple

values=[10,20,30,40]
c=tuple(values)
print(c)