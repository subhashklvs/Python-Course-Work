# 1. Integer – student roll number
roll_number = int(input("Enter roll number: "))

# 2. Float – student percentage
percentage = float(input("Enter percentage: "))

# 3. String – student name
student_name = input("Enter student name: ")

# 4. Dictionary – student address
address = {
    "city": input("Enter city: "),
    "state": input("Enter state: "),
    "pincode": input("Enter pincode: ")
}

# 5. List – subjects taken
subjects = input("Enter subjects (comma separated): ").split(",")

# 6. Tuple – date of birth (day, month, year)
dob = tuple(input("Enter date of birth (DD,MM,YYYY): ").split(","))

# 7. Set – skills (unique values)
skills = set(input("Enter skills (comma separated): ").split(","))

print("\n--- STUDENT DETAILS ---")
print("Roll Number:", roll_number, type(roll_number))
print("Percentage:", percentage, type(percentage))
print("Student Name:", student_name, type(student_name))
print("Address:", address, type(address))
print("Subjects:", subjects, type(subjects))
print("Date of Birth:", dob, type(dob))
print("Skills:", skills, type(skills))
