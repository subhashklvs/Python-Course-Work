# without function :
n=121
temp=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")
    
# with function :

def is_palindrome(n):
    temp=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if temp==rev:
        return "palindrome"
    else:
        return "not palindrome"
print(is_palindrome(121))