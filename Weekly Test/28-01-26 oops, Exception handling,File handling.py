# 1. Exception handling-instagram login system :

class AgeError(Exception):
    pass
try:
    age = int(input())
    if age < 13:
        raise AgeError("Minimum age requirement is 13.")
    else:
        print("Account created successfully.")
except ValueError:
    print("Invalid input. Please enter a valid age.")
except AgeError as e:
    print(e)

# 2. File handling-you tube video log : 

title = input()
with open("youtube_log.txt", "a") as file:
    file.write(title + "\n")
print("Video added successfully.")
print("Stored Videos:")
with open("youtube_log.txt", "r") as file:
    for line in file:
        print(line.strip())

# 3. oops-linkedln profile class :

class LinkedInProfile:
    platform = "LinkedIn"
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def display_profile(self):
        print(f"Platform: {LinkedInProfile.platform}")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
    @staticmethod
    def platform_rules():
        print("Maintain professional behavior.")
name = input()
role = input()
profile = LinkedInProfile(name, role)
profile.display_profile()
LinkedInProfile.platform_rules()

# Encapsulation - hotstar subscription :

class HotstarAccount:
    def __init__(self):
        self.__subscription_status = "Inactive"
    def check_status(self):
        print(f"Subscription Status: {self.__subscription_status}")
    def activate_subscription(self):
        print("Activating subscription...")
        self.__subscription_status = "Active"
account = HotstarAccount()
account.check_status()
account.activate_subscription()
account.check_status()

# 5. single inheritance - start employee system :

class StartupEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")
class Developer(StartupEmployee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.language}")
name = input()
salary = int(input())
language = input()
dev = Developer(name, salary, language)
dev.display_details()

#
a=0
b=1
for i in range(8):
    print(a,end=" ")
    a,b=b,a+b

a=5
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)