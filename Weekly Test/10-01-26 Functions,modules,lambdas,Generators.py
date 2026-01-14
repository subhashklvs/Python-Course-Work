# 1.Calculate circle proprties (Math module) :

import math
def circle_values(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return (round(area, 2), round(circumference, 2))

# 2.Random Password Generator (Random module) :

import random
def generate_password(length):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

# 3. Filter passed students (Using lambda+filter) :

def passed_students(marks):
    return list(filter(lambda x: x >= 40, marks))

# 4.Check Prime Number (Recursion) :

def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

# 5.Find power of a number(Recursion) :

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# 6.Filter Emails by Domains(lambda):

def filter_emails(emails, domain):
    return list(filter(lambda x: x.endswith(domain), emails))

# 7. Create your own utility module (user defined Modules) :

def is_positive(n):
    return n > 0

def sum_of_numbers(lst):
    return sum(lst)

print(is_positive(5))
print(sum_of_numbers([1, 2, 3, 4]))

# 8.Remove Duplicate numbers(set+lambda):

def remove_duplicates(nums):
    return sorted(set(nums))

# 9.Countdown Generator(Generators) :

def countdown(n):
    while n > 0:
        yield n
        n -= 1

# 10.Sum of nested list(Recursion) :

def nested_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total





