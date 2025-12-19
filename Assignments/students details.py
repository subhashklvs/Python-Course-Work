# 1. Integer – employee ID
employee_id = int(input("Enter employee ID: "))

# 2. Float – employee salary
salary = float(input("Enter monthly salary: "))

# 3. String – employee name
employee_name = input("Enter employee name: ")

# 4. Dictionary – employee address
employee_address = {
    "house_no": input("Enter house number: "),
    "street": input("Enter street name: "),
    "city": input("Enter city: ")
}

# 5. List – employee skills
skills = input("Enter skills (comma separated): ").split(",")

# 6. Tuple – joining date (DD, MM, YYYY)
joining_date = tuple(input("Enter joining date (DD,MM,YYYY): ").split(","))

# 7. Set – project names (unique projects)
projects = set(input("Enter project names (comma separated): ").split(","))

print("--- EMPLOYEE DETAILS ---")
print("Employee ID:", employee_id, type(employee_id))
print("Salary:", salary, type(salary))
print("Employee Name:", employee_name, type(employee_name))
print("Address:", employee_address, type(employee_address))
print("Skills:", skills, type(skills))
print("Joining Date:", joining_date, type(joining_date))
print("Projects:", projects, type(projects))
