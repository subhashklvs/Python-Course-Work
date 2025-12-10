# Strings in python

str1="kokkirala"
str2="lakshmivenkatasaisubhash"
print(str1+str2)            #concatenation
print(str1*3)               #repatition
print(str2[8])              #Indexing
print(str2[1:3])            #Slicing     
print("subhash" in str2)    # Membership

# methods()

print(str1.upper())         #upper()
print(str1.lower())         #lower()
print(str1.capitalize())    #capitalize()
print(str1.title())         #title()
print(str1.swapcase())      #swapcase()
print(str1.center(30,'*'))  #center()
print(str1.ljust(35,'*'))   #ljust()
print(str1.rjust(53,'*'))   #rjust()
print('100'.zfill(30))      #zfill()
print(str1.find('0'))       #find() - if there is no letter it print -1
print(str1.rfind('a'))      #rfind()
print(str1.index('k'))      #index() - if there is no letter it print Error
print(str1.rindex('k'))     #rindex()
print(str1.count('k'))      #count()
print(str2.replace('s','*')) #replace()
print(str2.translate('h','*'))