"""
===========================================================
Chapter - Variables
===========================================================

Description :
This file demonstrates Python variables, naming conventions,
multiple assignments, dynamic typing, constants, and best
practices.

===========================================================
"""

# ==========================================================
# 1. What is a Variable?
# ==========================================================

print("=" * 60)
print("1. VARIABLES")
print("=" * 60)

name = "Ram"
age = 25
salary = 45000.50
is_employee = True

print(f"Name      : {name}")
print(f"Age       : {age}")
print(f"Salary    : {salary}")
print(f"Employee? : {is_employee}")


# ==========================================================
# 2. Variable Naming Rules
# ==========================================================

print("\n" + "=" * 60)
print("2. VARIABLE NAMING")
print("=" * 60)

student_name = "Shyam"
student_age = 22
total_marks = 485

print(student_name)
print(student_age)
print(total_marks)

# Valid names
city = "Mumbai"
_city = "Pune"
city1 = "Delhi"
student_name_1 = "Krishna"

print(city)
print(_city)
print(city1)
print(student_name_1)

# Invalid examples (commented intentionally)
#
# 1city = "Mumbai"
# student-name = "Shyam"
# class = "Python"


# ==========================================================
# 3. Dynamic Typing
# ==========================================================

print("\n" + "=" * 60)
print("3. DYNAMIC TYPING")
print("=" * 60)

value = 100
print(value)
print(type(value))

value = "Python"

print(value)
print(type(value))

value = 10.5

print(value)
print(type(value))


# ==========================================================
# 4. Multiple Assignment
# ==========================================================

print("\n" + "=" * 60)
print("4. MULTIPLE ASSIGNMENT")
print("=" * 60)

x, y, z = 10, 20, 30

print(x)
print(y)
print(z)


# ==========================================================
# 5. Same Value Assignment
# ==========================================================

print("\n" + "=" * 60)
print("5. SAME VALUE ASSIGNMENT")
print("=" * 60)

a = b = c = 100

print(a)
print(b)
print(c)


# ==========================================================
# 6. Swapping Variables
# ==========================================================

print("\n" + "=" * 60)
print("6. SWAPPING VARIABLES")
print("=" * 60)

num1 = 5
num2 = 10

print("Before Swap")
print(num1, num2)

num1, num2 = num2, num1

print("After Swap")
print(num1, num2)


# ==========================================================
# 7. Constants (Convention)
# ==========================================================

print("\n" + "=" * 60)
print("7. CONSTANTS")
print("=" * 60)

PI = 3.14159
MAX_USERS = 500

print(PI)
print(MAX_USERS)


# ==========================================================
# 8. Deleting Variables
# ==========================================================

print("\n" + "=" * 60)
print("8. DELETE VARIABLE")
print("=" * 60)

temp = "Temporary Variable"

print(temp)

del temp

# print(temp)
# Uncommenting the line above will raise NameError.


# ==========================================================
# 9. Checking Variable Types
# ==========================================================

print("\n" + "=" * 60)
print("9. TYPE CHECKING")
print("=" * 60)

number = 10
price = 100.75
language = "Python"
status = True

print(type(number))
print(type(price))
print(type(language))
print(type(status))


# ==========================================================
# 10. Identity (id)
# ==========================================================

print("\n" + "=" * 60)
print("10. MEMORY ID")
print("=" * 60)

x = 100
y = 100

print(id(x))
print(id(y))

print(x is y)


# ==========================================================
# 11. Variable Scope Preview
# ==========================================================

print("\n" + "=" * 60)
print("11. VARIABLE SCOPE")
print("=" * 60)

message = "Global Variable"


def display():
    local_message = "Local Variable"

    print(message)
    print(local_message)


display()


# ==========================================================
# 12. Best Practices
# ==========================================================

print("\n" + "=" * 60)
print("12. BEST PRACTICES")
print("=" * 60)

student_count = 150
average_marks = 82.5
course_name = "Python Fundamentals"

print(student_count)
print(average_marks)
print(course_name)


# ==========================================================
# End
# ==========================================================

print("\n" + "=" * 60)
print("Variables chapter completed successfully.")
print("=" * 60)