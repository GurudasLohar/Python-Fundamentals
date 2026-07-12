"""
=====================================================================
Python Fundamentals
Chapter : Data Types

Topics Covered
--------------
1. Introduction to Data Types
2. type() Function
3. Integer (int)
4. Float (float)
5. Complex (complex)
6. Numeric Operations
7. Type Conversion

=====================================================================
"""

# ===================================================================
# SECTION 1 : INTRODUCTION TO DATA TYPES
# ===================================================================

print("=" * 70)
print("SECTION 1 : INTRODUCTION TO DATA TYPES")
print("=" * 70)

"""
A data type defines the kind of value stored in a variable.

Python automatically identifies the data type based on the assigned value.

Examples:
Integer  -> 10
Float    -> 3.14
String   -> "Python"
Boolean  -> True
"""

age = 25
height = 5.9
language = "Python"
is_student = True

print("Age      :", age)
print("Height   :", height)
print("Language :", language)
print("Student  :", is_student)

print()


# ===================================================================
# SECTION 2 : type() FUNCTION
# ===================================================================

print("=" * 70)
print("SECTION 2 : type() FUNCTION")
print("=" * 70)

"""
The type() function returns the data type of an object.
"""

print(type(age))
print(type(height))
print(type(language))
print(type(is_student))

print()

number = 100
price = 250.75
course = "Python Fundamentals"

print(f"{number} -> {type(number)}")
print(f"{price} -> {type(price)}")
print(f"{course} -> {type(course)}")

print()


# ===================================================================
# SECTION 3 : INTEGER (int)
# ===================================================================

print("=" * 70)
print("SECTION 3 : INTEGER")
print("=" * 70)

"""
An integer is a whole number.

Examples:
-100
0
25
50000

Integers have unlimited precision in Python.
"""

positive = 150
negative = -90
zero = 0
large_number = 123456789012345678901234567890

print("Positive Integer :", positive)
print("Negative Integer :", negative)
print("Zero             :", zero)
print("Large Number     :", large_number)

print()

print("Type :", type(positive))

print()


# Integer arithmetic

a = 15
b = 4

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Power          :", a ** b)

print()


# ===================================================================
# SECTION 4 : FLOAT (float)
# ===================================================================

print("=" * 70)
print("SECTION 4 : FLOAT")
print("=" * 70)

"""
A float represents decimal numbers.

Examples:
3.14
100.5
-25.75
"""

pi = 3.14159265
temperature = 36.8
salary = 78500.50

print("PI          :", pi)
print("Temperature :", temperature)
print("Salary      :", salary)

print()

print(type(pi))

print()


x = 25.5
y = 10.2

print("Addition       :", x + y)
print("Subtraction    :", x - y)
print("Multiplication :", x * y)
print("Division       :", x / y)

print()


# ===================================================================
# SECTION 5 : COMPLEX NUMBERS
# ===================================================================

print("=" * 70)
print("SECTION 5 : COMPLEX NUMBERS")
print("=" * 70)

"""
Complex numbers consist of:

Real Part
Imaginary Part

Syntax:

a + bj

Example:

5 + 6j
"""

complex1 = 4 + 5j
complex2 = 2 + 3j

print("Complex Number 1 :", complex1)
print("Complex Number 2 :", complex2)

print()

print("Real Part      :", complex1.real)
print("Imaginary Part :", complex1.imag)

print()

print("Addition       :", complex1 + complex2)
print("Subtraction    :", complex1 - complex2)
print("Multiplication :", complex1 * complex2)

print()


# ===================================================================
# SECTION 6 : NUMERIC OPERATIONS
# ===================================================================

print("=" * 70)
print("SECTION 6 : NUMERIC OPERATIONS")
print("=" * 70)

num1 = 25
num2 = 8

print("Addition       :", num1 + num2)
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division       :", num1 / num2)
print("Floor Division :", num1 // num2)
print("Modulus        :", num1 % num2)
print("Exponent       :", num1 ** num2)

print()

print("Absolute Value :", abs(-75))
print("Maximum        :", max(10, 50, 30))
print("Minimum        :", min(10, 50, 30))
print("Round          :", round(12.6789, 2))

print()


# ===================================================================
# SECTION 7 : TYPE CONVERSION
# ===================================================================

print("=" * 70)
print("SECTION 7 : TYPE CONVERSION")
print("=" * 70)

"""
Python allows conversion between compatible data types.
"""

integer_value = 25
float_value = 15.75
string_number = "100"

print("Original Values")
print(integer_value, type(integer_value))
print(float_value, type(float_value))
print(string_number, type(string_number))

print()

# Integer to Float

converted_float = float(integer_value)

print("Integer -> Float")
print(converted_float)
print(type(converted_float))

print()

# Float to Integer

converted_integer = int(float_value)

print("Float -> Integer")
print(converted_integer)
print(type(converted_integer))

print()

# String to Integer

converted_string = int(string_number)

print("String -> Integer")
print(converted_string)
print(type(converted_string))

print()

# Integer to String

text = str(integer_value)

print("Integer -> String")
print(text)
print(type(text))

print()

# Float to String

text2 = str(float_value)

print(text2)
print(type(text2))

# ===================================================================
# SECTION 1 : BOOLEAN DATA TYPE
# ===================================================================

print("=" * 70)
print("SECTION 1 : BOOLEAN (bool)")
print("=" * 70)

"""
A Boolean data type has only two possible values:

True
False

Boolean values are commonly used in:

✔ Decision making
✔ Conditions
✔ Loops
✔ Comparisons
"""

is_logged_in = True
is_admin = False

print("Is Logged In :", is_logged_in)
print("Is Admin     :", is_admin)

print()

print("Data Type of is_logged_in :", type(is_logged_in))
print("Data Type of is_admin     :", type(is_admin))

print()


# ===================================================================
# Boolean Comparisons
# ===================================================================

print("=" * 70)
print("BOOLEAN COMPARISON")
print("=" * 70)

age = 20

print(age >= 18)
print(age < 18)

print(10 == 10)
print(10 != 5)

print(20 > 10)
print(20 < 10)

print()


# ===================================================================
# SECTION 2 : TRUTHY AND FALSY VALUES
# ===================================================================

print("=" * 70)
print("SECTION 2 : TRUTHY AND FALSY VALUES")
print("=" * 70)

"""
Python treats some values as False
and all other values as True.

Falsy Values

False
None
0
0.0
''
[]
{}
set()

Everything else is Truthy.
"""

print("Falsy Examples")

print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(None))

print()

print("Truthy Examples")

print(bool(10))
print(bool(-5))
print(bool(3.14))
print(bool("Python"))
print(bool([1, 2, 3]))
print(bool({"Name": "Alice"}))

print()


# ===================================================================
# SECTION 3 : LOGICAL OPERATORS
# ===================================================================

print("=" * 70)
print("SECTION 3 : LOGICAL OPERATORS")
print("=" * 70)

"""
Python supports three logical operators.

and
or
not
"""

x = True
y = False

print("AND")
print(x and y)
print(True and True)
print(False and True)

print()

print("OR")
print(x or y)
print(False or False)
print(True or False)

print()

print("NOT")
print(not x)
print(not y)

print()


# Example

age = 22
salary = 45000

eligible = age >= 18 and salary >= 30000

print("Eligible :", eligible)

print()


# ===================================================================
# SECTION 4 : STRING DATA TYPE
# ===================================================================

print("=" * 70)
print("SECTION 4 : STRING (str)")
print("=" * 70)

"""
A string is a sequence of Unicode characters.

Strings are enclosed within:

''
""

or

'''
'''

"""

name = "Alice"
city = 'Mumbai'

print(name)
print(city)

print()

print(type(name))

print()


# ===================================================================
# SECTION 5 : CREATING STRINGS
# ===================================================================

print("=" * 70)
print("SECTION 5 : CREATING STRINGS")
print("=" * 70)

language = "Python"

course = 'Python Fundamentals'

message = """Welcome to
Python Programming"""

print(language)

print(course)

print(message)

print()


# Empty String

empty = ""

print(empty)

print(type(empty))

print()


# ===================================================================
# Different Quotes
# ===================================================================

single = 'Single Quote'

double = "Double Quote"

triple = """Triple Quote"""

print(single)
print(double)
print(triple)

print()


# ===================================================================
# SECTION 6 : ESCAPE CHARACTERS
# ===================================================================

print("=" * 70)
print("SECTION 6 : ESCAPE CHARACTERS")
print("=" * 70)

"""
Escape Characters begin with a backslash (\)

Common Escape Characters

\\n  New Line
\\t  Tab
\\\\  Backslash
\\'  Single Quote
\\"  Double Quote
"""

print("Python\nProgramming")

print()

print("Name\tAge\tCity")

print()

print("Folder : C:\\Users\\Admin")

print()

print('It\'s a beautiful day.')

print()

print("She said, \"Python is awesome!\"")

print()


# ===================================================================
# Raw String
# ===================================================================

print("=" * 70)
print("RAW STRING")
print("=" * 70)

path = r"C:\Users\Admin\Documents\Python"

print(path)

print()


# ===================================================================
# SECTION 7 : MULTILINE STRINGS
# ===================================================================

print("=" * 70)
print("SECTION 7 : MULTILINE STRINGS")
print("=" * 70)

paragraph = """
Python is a high-level,
general-purpose programming language.

It is widely used in

• Data Science
• Artificial Intelligence
• Machine Learning
• Web Development
• Automation
"""

print(paragraph)

print()


# Another Example

html = """
<html>
    <head>
        <title>Python</title>
    </head>

    <body>

        <h1>Hello Python</h1>

    </body>

</html>
"""

print(html)

print()


# ===================================================================
# Practical Example
# ===================================================================

print("=" * 70)
print("PRACTICAL EXAMPLE")
print("=" * 70)

student_name = "Rahul"
course = "Python Fundamentals"
marks = 92

print("Student :", student_name)
print("Course  :", course)
print("Marks   :", marks)

passed = marks >= 40

print("Passed  :", passed)

print()

# ===================================================================
# SECTION 1 : STRING CONCATENATION
# ===================================================================

print("=" * 70)
print("SECTION 1 : STRING CONCATENATION")
print("=" * 70)

"""
String Concatenation means joining two or more strings
using the + operator.
"""

first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name

print("First Name :", first_name)
print("Last Name  :", last_name)
print("Full Name  :", full_name)

print()

# --------------------------------------------------------------

city = "Mumbai"
state = "Maharashtra"
country = "India"

address = city + ", " + state + ", " + country

print("Address :", address)

print()

# --------------------------------------------------------------

greeting = "Hello"
message = "Welcome"

result = greeting + " " + message

print(result)

print()

# --------------------------------------------------------------

print("=" * 70)
print("CONCATENATION WITH VARIABLES")
print("=" * 70)

language = "Python"
version = "3.14"

print("Learning " + language)
print(language + " Version " + version)

print()

# --------------------------------------------------------------

print("=" * 70)
print("COMMON MISTAKE")
print("=" * 70)

"""
Numbers cannot be concatenated directly with strings.
"""

age = 25

# print("Age : " + age)     # Error

print("Correct Example")

print("Age :", age)

print("Age : " + str(age))

print()


# ===================================================================
# SECTION 2 : STRING REPETITION
# ===================================================================

print("=" * 70)
print("SECTION 2 : STRING REPETITION")
print("=" * 70)

"""
The * operator repeats a string.
"""

print("Python " * 5)

print()

print("*" * 50)

print()

print("=" * 40)

print()

symbol = "-"

print(symbol * 60)

print()

word = "AI"

print(word * 8)

print()

# --------------------------------------------------------------

print("=" * 70)
print("PRACTICAL EXAMPLE")
print("=" * 70)

print("=" * 40)

print("WELCOME")

print("=" * 40)

print()

# ===================================================================
# SECTION 3 : STRING INDEXING
# ===================================================================

print("=" * 70)
print("SECTION 3 : STRING INDEXING")
print("=" * 70)

"""
Each character in a string has an index.

Example

P y t h o n

0 1 2 3 4 5
"""

language = "Python"

print(language)

print()

print("Index 0 :", language[0])
print("Index 1 :", language[1])
print("Index 2 :", language[2])
print("Index 3 :", language[3])
print("Index 4 :", language[4])
print("Index 5 :", language[5])

print()

# --------------------------------------------------------------

student = "Rahul"

print(student[0])
print(student[1])
print(student[2])
print(student[3])
print(student[4])

print()

# --------------------------------------------------------------

print("=" * 70)
print("LENGTH OF STRING")
print("=" * 70)

print(language)

print("Length :", len(language))

print()

# --------------------------------------------------------------

print("=" * 70)
print("INDEX OUT OF RANGE")
print("=" * 70)

"""
Trying to access an invalid index causes an IndexError.
"""

print(language[5])

# print(language[10])

print()

# ===================================================================
# SECTION 4 : NEGATIVE INDEXING
# ===================================================================

print("=" * 70)
print("SECTION 4 : NEGATIVE INDEXING")
print("=" * 70)

"""
Python supports negative indexing.

P  y  t  h  o  n

0  1  2  3  4  5

-6 -5 -4 -3 -2 -1
"""

language = "Python"

print(language)

print()

print("Last Character       :", language[-1])
print("Second Last          :", language[-2])
print("Third Last           :", language[-3])
print("Fourth Last          :", language[-4])
print("Fifth Last           :", language[-5])
print("Sixth Last           :", language[-6])

print()

# --------------------------------------------------------------

name = "Artificial Intelligence"

print("Last Letter :", name[-1])

print("Second Last :", name[-2])

print("Third Last  :", name[-3])

print()

# --------------------------------------------------------------

print("=" * 70)
print("POSITIVE VS NEGATIVE INDEX")
print("=" * 70)

text = "Python"

print("Positive Index")

for i in range(len(text)):
    print(f"{i} -> {text[i]}")

print()

print("Negative Index")

for i in range(1, len(text) + 1):
    print(f"-{i} -> {text[-i]}")

print()

# ===================================================================
# PRACTICAL EXAMPLE
# ===================================================================

print("=" * 70)
print("PRACTICAL EXAMPLE")
print("=" * 70)

course = "Python Fundamentals"

print("Course :", course)

print("First Character :", course[0])

print("Last Character :", course[-1])

print("Length :", len(course))

print()

# =====================================================================
# Basic Slicing
# =====================================================================

print("\n" + "=" * 70)
print("1. BASIC STRING SLICING")
print("=" * 70)

print("language[0:6]  :", language[0:6])
print("language[7:18] :", language[7:18])
print("language[0:18] :", language[0:18])

# =====================================================================
# Omitting Start Index
# =====================================================================

print("\n" + "=" * 70)
print("2. OMITTING START INDEX")
print("=" * 70)

print("language[:6]   :", language[:6])
print("language[:10]  :", language[:10])

# =====================================================================
# Omitting Stop Index
# =====================================================================

print("\n" + "=" * 70)
print("3. OMITTING STOP INDEX")
print("=" * 70)

print("language[7:]   :", language[7:])
print("language[10:]  :", language[10:])

# =====================================================================
# Complete Copy
# =====================================================================

print("\n" + "=" * 70)
print("4. COPYING A STRING")
print("=" * 70)

copy_text = language[:]

print("Original :", language)
print("Copied   :", copy_text)

# =====================================================================
# Step Value
# =====================================================================

print("\n" + "=" * 70)
print("5. STEP VALUE")
print("=" * 70)

text = "ABCDEFGHIJK"

print("Original :", text)

print()

print("Every Character")
print(text[::1])

print()

print("Every Second Character")
print(text[::2])

print()

print("Every Third Character")
print(text[::3])

print()

print("Every Fourth Character")
print(text[::4])

# =====================================================================
# Negative Slicing
# =====================================================================

print("\n" + "=" * 70)
print("6. NEGATIVE SLICING")
print("=" * 70)

name = "Artificial Intelligence"

print("Original :", name)

print()

print("Last 5 Characters")
print(name[-5:])

print()

print("Without Last Character")
print(name[:-1])

print()

print("Last 10 Characters")
print(name[-10:])

# =====================================================================
# Reverse String
# =====================================================================

print("\n" + "=" * 70)
print("7. REVERSE STRING")
print("=" * 70)

word = "Python"

print("Original :", word)
print("Reverse  :", word[::-1])

sentence = "Machine Learning"

print()

print(sentence)
print(sentence[::-1])

# =====================================================================
# Extracting Words
# =====================================================================

print("\n" + "=" * 70)
print("8. EXTRACTING WORDS")
print("=" * 70)

course = "Python Fundamentals"

print(course)

print()

first_word = course[:6]
second_word = course[7:]

print("First Word :", first_word)
print("Second Word:", second_word)

# =====================================================================
# Slicing Numbers Stored as Strings
# =====================================================================

print("\n" + "=" * 70)
print("9. SLICING NUMERIC STRINGS")
print("=" * 70)

number = "9876543210"

print("Original :", number)

print()

print("First Four :", number[:4])
print("Last Four  :", number[-4:])
print("Middle     :", number[3:7])

# =====================================================================
# Email Username Example
# =====================================================================

print("\n" + "=" * 70)
print("10. PRACTICAL EXAMPLE - EMAIL")
print("=" * 70)

email = "student@gmail.com"

username = email[:7]

print("Email    :", email)
print("Username :", username)

# =====================================================================
# Date Example
# =====================================================================

print("\n" + "=" * 70)
print("11. PRACTICAL EXAMPLE - DATE")
print("=" * 70)

date = "15-08-2026"

day = date[:2]
month = date[3:5]
year = date[6:]

print("Date :", date)
print("Day  :", day)
print("Month:", month)
print("Year :", year)

# =====================================================================
# File Extension Example
# =====================================================================

print("\n" + "=" * 70)
print("12. PRACTICAL EXAMPLE - FILE")
print("=" * 70)

filename = "report.pdf"

extension = filename[-3:]

print("Filename :", filename)
print("Extension:", extension)

# =====================================================================
# Common Mistakes
# =====================================================================

print("\n" + "=" * 70)
print("13. COMMON MISTAKES")
print("=" * 70)

"""
Incorrect

text[10]

If index 10 does not exist,
Python raises IndexError.

Slicing is different.

text[10:20]

returns an empty string
instead of an error.
"""

sample = "Python"

print("sample[10:20] ->", sample[10:20])

# print(sample[10])   # IndexError

# =====================================================================
# SECTION 1 : INTRODUCTION
# =====================================================================

print("=" * 70)
print("MEMBERSHIP OPERATORS")
print("=" * 70)

"""
Membership operators are used to check whether
a value exists inside a collection.

Python provides two membership operators:

1. in
2. not in

They return Boolean values (True or False).
"""

# =====================================================================
# SECTION 2 : IN OPERATOR
# =====================================================================

print("\n" + "=" * 70)
print("1. IN OPERATOR")
print("=" * 70)

language = "Python"

print("Python" in "I love Python Programming")
print("Java" in "I love Python Programming")

print()

print("P" in language)
print("y" in language)
print("z" in language)

# =====================================================================
# SECTION 3 : NOT IN OPERATOR
# =====================================================================

print("\n" + "=" * 70)
print("2. NOT IN OPERATOR")
print("=" * 70)

print("Java" not in language)
print("Python" not in language)

print()

print("x" not in language)
print("P" not in language)

# =====================================================================
# SECTION 4 : MEMBERSHIP IN STRINGS
# =====================================================================

print("\n" + "=" * 70)
print("3. MEMBERSHIP IN STRINGS")
print("=" * 70)

sentence = "Python is easy to learn"

print("'Python' exists :", "Python" in sentence)
print("'easy' exists   :", "easy" in sentence)
print("'Java' exists   :", "Java" in sentence)

print()

print("'python' exists :", "python" in sentence)

print("\nStrings are CASE-SENSITIVE.")

# =====================================================================
# SECTION 5 : MEMBERSHIP IN LISTS
# =====================================================================

print("\n" + "=" * 70)
print("4. MEMBERSHIP IN LISTS")
print("=" * 70)

numbers = [10, 20, 30, 40, 50]

print(numbers)

print()

print(20 in numbers)
print(60 in numbers)

print()

print(60 not in numbers)
print(10 not in numbers)

# =====================================================================
# SECTION 6 : MEMBERSHIP IN TUPLES
# =====================================================================

print("\n" + "=" * 70)
print("5. MEMBERSHIP IN TUPLES")
print("=" * 70)

colors = ("Red", "Green", "Blue")

print(colors)

print()

print("Green" in colors)
print("Black" in colors)

print()

print("Black" not in colors)

# =====================================================================
# SECTION 7 : MEMBERSHIP IN SETS
# =====================================================================

print("\n" + "=" * 70)
print("6. MEMBERSHIP IN SETS")
print("=" * 70)

fruits = {"Apple", "Mango", "Orange", "Banana"}

print(fruits)

print()

print("Apple" in fruits)
print("Grapes" in fruits)

print()

print("Banana" not in fruits)

# =====================================================================
# SECTION 8 : MEMBERSHIP IN DICTIONARIES
# =====================================================================

print("\n" + "=" * 70)
print("7. MEMBERSHIP IN DICTIONARIES")
print("=" * 70)

student = {
    "name": "Rahul",
    "age": 21,
    "city": "Mumbai"
}

print(student)

print()

print("name" in student)
print("age" in student)
print("marks" in student)

print()

print("Rahul" in student)

print()

print("Rahul" in student.values())
print("Mumbai" in student.values())

# =====================================================================
# SECTION 9 : PRACTICAL EXAMPLE
# =====================================================================

print("\n" + "=" * 70)
print("8. PRACTICAL EXAMPLE")
print("=" * 70)

allowed_languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

user_choice = "Python"

if user_choice in allowed_languages:
    print(user_choice, "is available.")
else:
    print(user_choice, "is not available.")

print()

# =====================================================================
# Email Validation
# =====================================================================

email = "student@gmail.com"

print("Email :", email)

if "@" in email:
    print("Valid Email Format")
else:
    print("Invalid Email")

print()

# =====================================================================
# Password Check
# =====================================================================

password = "Python@123"

print("Password :", password)

if "@" in password:
    print("Contains Special Symbol")
else:
    print("No Special Symbol")

print()

# =====================================================================
# SECTION 10 : CASE SENSITIVITY
# =====================================================================

print("\n" + "=" * 70)
print("9. CASE SENSITIVITY")
print("=" * 70)

text = "Python"

print("python" in text)
print("Python" in text)

print()

print("python" in text.lower())

# =====================================================================
# SECTION 1 : INTRODUCTION
# =====================================================================

print("=" * 70)
print("STRING IMMUTABILITY")
print("=" * 70)

"""
A string is an IMMUTABLE object.

Immutable means:

Once a string is created,
its individual characters cannot be changed.

If you perform an operation on a string,
Python creates a NEW string object.
"""

text = "Python"

print("Original String :", text)
print("Memory ID       :", id(text))

# =====================================================================
# SECTION 2 : ATTEMPTING TO MODIFY A STRING
# =====================================================================

print("\n" + "=" * 70)
print("ATTEMPTING TO MODIFY A STRING")
print("=" * 70)

"""
The following statement would raise a TypeError:

text[0] = "J"

Reason:
Strings do not support item assignment.
"""

sample = "Python"

print("Original :", sample)

# Uncomment the next line to observe the error.
# sample[0] = "J"

print("Result : Strings cannot be modified using indexing.")

# =====================================================================
# SECTION 3 : CREATING A NEW STRING
# =====================================================================

print("\n" + "=" * 70)
print("CREATING A NEW STRING")
print("=" * 70)

language = "Python"

print("Before :", language)
print("ID     :", id(language))

language = "Java"

print()
print("After  :", language)
print("ID     :", id(language))

print("""
Notice that the memory ID changed.
Python created a NEW string object.
""")

# =====================================================================
# SECTION 4 : USING CONCATENATION
# =====================================================================

print("\n" + "=" * 70)
print("CONCATENATION CREATES A NEW STRING")
print("=" * 70)

word = "Data"

print("Original :", word)
print("ID       :", id(word))

word = word + " Science"

print()
print("Updated  :", word)
print("ID       :", id(word))

# =====================================================================
# SECTION 5 : STRING METHODS
# =====================================================================

print("\n" + "=" * 70)
print("STRING METHODS")
print("=" * 70)

name = "python"

print("Original :", name)
print("ID       :", id(name))

upper_name = name.upper()

print()
print("Upper    :", upper_name)
print("ID       :", id(upper_name))

print()
print("Original remains unchanged :", name)

print("""
Methods like upper(), lower(), replace(), and strip()
return NEW strings instead of modifying the original.
""")

# =====================================================================
# SECTION 6 : REPLACE METHOD
# =====================================================================

print("\n" + "=" * 70)
print("REPLACE METHOD")
print("=" * 70)

message = "I like Java"

print("Original :", message)

updated_message = message.replace("Java", "Python")

print("Updated  :", updated_message)
print("Original :", message)

# =====================================================================
# SECTION 7 : OBJECT IDENTITY
# =====================================================================

print("\n" + "=" * 70)
print("OBJECT IDENTITY")
print("=" * 70)

text1 = "Python"
text2 = text1

print("text1 :", text1)
print("text2 :", text2)

print()

print("ID of text1 :", id(text1))
print("ID of text2 :", id(text2))

print()

text2 = text2 + " Programming"

print("After Modification")
print()

print("text1 :", text1)
print("text2 :", text2)

print()

print("ID of text1 :", id(text1))
print("ID of text2 :", id(text2))

# =====================================================================
# SECTION 8 : PRACTICAL EXAMPLE
# =====================================================================

print("\n" + "=" * 70)
print("PRACTICAL EXAMPLE")
print("=" * 70)

username = "admin"

print("Original Username :", username)

formatted_username = username.capitalize()

print("Formatted Username:", formatted_username)
print("Original Username :", username)


# =====================================================================
# SECTION 1 : strip()
# =====================================================================

print("\n" + "=" * 70)
print("1. strip()")
print("=" * 70)

"""
strip() removes leading and trailing whitespace.

Syntax:
string.strip()
"""

text = "   Python Programming   "

print("Original :", repr(text))
print("After strip():", repr(text.strip()))

print("\nOriginal string remains unchanged:")
print(repr(text))

# =====================================================================
# SECTION 2 : lstrip()
# =====================================================================

print("\n" + "=" * 70)
print("2. lstrip()")
print("=" * 70)

"""
lstrip() removes whitespace only from the left side.
"""

text = "     Data Science"

print("Original :", repr(text))
print("After lstrip():", repr(text.lstrip()))

# =====================================================================
# SECTION 3 : rstrip()
# =====================================================================

print("\n" + "=" * 70)
print("3. rstrip()")
print("=" * 70)

"""
rstrip() removes whitespace only from the right side.
"""

text = "Machine Learning      "

print("Original :", repr(text))
print("After rstrip():", repr(text.rstrip()))

# =====================================================================
# SECTION 4 : Removing Specific Characters
# =====================================================================

print("\n" + "=" * 70)
print("4. Removing Specific Characters")
print("=" * 70)

"""
strip(), lstrip(), and rstrip() can remove
specified characters from both ends.

Syntax:
string.strip(chars)
"""

text = "***Python***"

print("Original :", text)
print("strip('*') :", text.strip("*"))

text = "###Welcome###"

print("\nOriginal :", text)
print("strip('#') :", text.strip("#"))

# =====================================================================
# SECTION 5 : replace()
# =====================================================================

print("\n" + "=" * 70)
print("5. replace()")
print("=" * 70)

"""
replace(old, new)

Replaces all occurrences of 'old'
with 'new'.

Returns a NEW string.
"""

sentence = "I love Java"

print("Original :", sentence)

updated = sentence.replace("Java", "Python")

print("Updated  :", updated)
print("Original :", sentence)

# =====================================================================
# SECTION 6 : Replace Multiple Occurrences
# =====================================================================

print("\n" + "=" * 70)
print("6. Replace Multiple Occurrences")
print("=" * 70)

text = "apple apple apple"

print("Original :", text)
print("Updated  :", text.replace("apple", "orange"))

# =====================================================================
# SECTION 7 : Replace Limited Occurrences
# =====================================================================

print("\n" + "=" * 70)
print("7. Replace Limited Occurrences")
print("=" * 70)

"""
replace(old, new, count)

The optional 'count' parameter limits
the number of replacements.
"""

text = "cat cat cat cat"

print("Original :", text)
print("Replace 1 :", text.replace("cat", "dog", 1))
print("Replace 2 :", text.replace("cat", "dog", 2))
print("Replace All :", text.replace("cat", "dog"))

# =====================================================================
# SECTION 8 : Practical Example - Username
# =====================================================================

print("\n" + "=" * 70)
print("8. Practical Example - Username")
print("=" * 70)

username = "   admin   "

print("Original :", repr(username))

clean_username = username.strip()

print("Cleaned  :", repr(clean_username))

# =====================================================================
# SECTION 9 : Practical Example - Phone Number
# =====================================================================

print("\n" + "=" * 70)
print("9. Practical Example - Phone Number")
print("=" * 70)

phone = "+91-98765-43210"

print("Original :", phone)

formatted_phone = phone.replace("-", "")

print("Formatted:", formatted_phone)

# =====================================================================
# SECTION 10 : Practical Example - File Name
# =====================================================================

print("\n" + "=" * 70)
print("10. Practical Example - File Name")
print("=" * 70)

filename = "report.docx"

print("Original :", filename)

pdf_file = filename.replace(".docx", ".pdf")

print("Converted:", pdf_file)

# =====================================================================
# SECTION 1 : split()
# =====================================================================

print("\n" + "=" * 70)
print("1. split()")
print("=" * 70)

"""
split() divides a string into a list.

Syntax:
string.split(separator)

Default separator is whitespace.
"""

sentence = "Python is easy to learn"

print("Original String:")
print(sentence)

words = sentence.split()

print("\nAfter split():")
print(words)

print("Data Type:", type(words))

# ---------------------------------------------------------------------

fruits = "Apple,Mango,Banana,Orange"

fruit_list = fruits.split(",")

print("\nOriginal :", fruits)
print("List     :", fruit_list)

# ---------------------------------------------------------------------

date = "15-08-2026"

date_parts = date.split("-")

print("\nDate :", date)
print("Split:", date_parts)

# =====================================================================
# SECTION 2 : join()
# =====================================================================

print("\n" + "=" * 70)
print("2. join()")
print("=" * 70)

"""
join() combines elements of an iterable into a string.

Syntax:
separator.join(iterable)
"""

languages = ["Python", "Java", "C++", "JavaScript"]

print("Original List:")
print(languages)

joined = ", ".join(languages)

print("\nJoined String:")
print(joined)

# ---------------------------------------------------------------------

letters = ["P", "Y", "T", "H", "O", "N"]

word = "".join(letters)

print("\nLetters :", letters)
print("Word    :", word)

# ---------------------------------------------------------------------

path = ["Users", "Admin", "Documents", "Python"]

full_path = "/".join(path)

print("\nPath :", full_path)

# =====================================================================
# SECTION 3 : find()
# =====================================================================

print("\n" + "=" * 70)
print("3. find()")
print("=" * 70)

"""
find() returns the index of the first occurrence
of a substring.

If the substring is not found,
it returns -1.
"""

text = "Python Programming"

print("Text :", text)

print("\nFind 'Python' :", text.find("Python"))
print("Find 'Programming' :", text.find("Programming"))
print("Find 'Java' :", text.find("Java"))

# ---------------------------------------------------------------------

sentence = "Machine Learning with Python"

print("\nSentence :", sentence)

position = sentence.find("Python")

print("Position :", position)

if position != -1:
    print("Substring Found")
else:
    print("Substring Not Found")

# =====================================================================
# SECTION 4 : count()
# =====================================================================

print("\n" + "=" * 70)
print("4. count()")
print("=" * 70)

"""
count() returns the number of occurrences
of a substring.
"""

text = "apple apple mango apple banana"

print("Text :", text)

print("\nCount of 'apple' :", text.count("apple"))
print("Count of 'banana':", text.count("banana"))
print("Count of 'grape' :", text.count("grape"))

# ---------------------------------------------------------------------

sentence = "Python Python Java Python"

print("\nSentence :", sentence)

print("Python appears :", sentence.count("Python"), "times")

# =====================================================================
# SECTION 5 : PRACTICAL EXAMPLES
# =====================================================================

print("\n" + "=" * 70)
print("5. PRACTICAL EXAMPLES")
print("=" * 70)

# Example 1 : Full Name

full_name = "John Michael Doe"

name_parts = full_name.split()

print("Full Name :", full_name)
print("First Name:", name_parts[0])
print("Last Name :", name_parts[-1])

# ---------------------------------------------------------------------

# Example 2 : CSV Data

csv_data = "101,Rahul,85"

student = csv_data.split(",")

print("\nCSV Data :", csv_data)
print("Roll No. :", student[0])
print("Name     :", student[1])
print("Marks    :", student[2])

# ---------------------------------------------------------------------

# Example 3 : Tags

tags = ["Python", "AI", "Machine Learning", "Data Science"]

tag_string = " | ".join(tags)

print("\nTags:")
print(tag_string)

# ---------------------------------------------------------------------

# Example 4 : Keyword Search

paragraph = "Python is powerful and Python is easy."

keyword = "Python"

print("\nParagraph:")
print(paragraph)

print("Occurrences:", paragraph.count(keyword))

# =====================================================================
# SECTION 1 : startswith()
# =====================================================================

print("\n" + "=" * 70)
print("1. startswith()")
print("=" * 70)

"""
startswith()

Checks whether a string begins with a specified prefix.

Syntax:
string.startswith(prefix)

Returns:
True  -> if the string starts with the prefix
False -> otherwise
"""

filename = "report.pdf"

print("Filename :", filename)

print()

print(filename.startswith("report"))
print(filename.startswith("data"))
print(filename.startswith("rep"))

# ------------------------------------------------------------

website = "https://www.python.org"

print()

print(website.startswith("https://"))
print(website.startswith("http://"))

# =====================================================================
# SECTION 2 : endswith()
# =====================================================================

print("\n" + "=" * 70)
print("2. endswith()")
print("=" * 70)

"""
endswith()

Checks whether a string ends with a suffix.

Syntax:
string.endswith(suffix)
"""

print(filename.endswith(".pdf"))
print(filename.endswith(".docx"))
print(filename.endswith(".txt"))

# ------------------------------------------------------------

image = "photo.png"

print()

print(image.endswith(".png"))
print(image.endswith(".jpg"))

# =====================================================================
# SECTION 3 : isalpha()
# =====================================================================

print("\n" + "=" * 70)
print("3. isalpha()")
print("=" * 70)

"""
isalpha()

Returns True only if all characters
are alphabetic.

Spaces, numbers and symbols
make it return False.
"""

name = "Python"

print(name.isalpha())

print()

print("Python3".isalpha())
print("Python Programming".isalpha())
print("Hello!".isalpha())

# =====================================================================
# SECTION 4 : isdigit()
# =====================================================================

print("\n" + "=" * 70)
print("4. isdigit()")
print("=" * 70)

"""
isdigit()

Returns True only if every character
is a digit.
"""

age = "25"

print(age.isdigit())

print()

print("123456".isdigit())
print("12.5".isdigit())
print("-100".isdigit())
print("ABC123".isdigit())

# =====================================================================
# SECTION 5 : isalnum()
# =====================================================================

print("\n" + "=" * 70)
print("5. isalnum()")
print("=" * 70)

"""
isalnum()

Returns True if every character
is either

Alphabet OR Number

No spaces
No symbols
"""

print("Python123".isalnum())

print()

print("Python".isalnum())
print("123".isalnum())
print("Python 123".isalnum())
print("Python@123".isalnum())

# =====================================================================
# SECTION 6 : isspace()
# =====================================================================

print("\n" + "=" * 70)
print("6. isspace()")
print("=" * 70)

"""
isspace()

Returns True if every character
is whitespace.
"""

print("   ".isspace())

print()

print("\t".isspace())
print("\n".isspace())
print("Python".isspace())
print(" Python ".isspace())


print("="*70)
print("STRING FORMATTING")
print("="*70)

# ==========================================================
# 1. f-Strings
# ==========================================================

name = "Alice"
age = 25

print(f"Name : {name}")
print(f"Age  : {age}")

# ==========================================================
# Expressions
# ==========================================================

a = 10
b = 20

print(f"Sum = {a+b}")
print(f"Product = {a*b}")

# ==========================================================
# Float Precision
# ==========================================================

pi = 3.1415926535

print(f"{pi:.2f}")
print(f"{pi:.4f}")

# ==========================================================
# Thousands Separator
# ==========================================================

salary = 1250000

print(f"{salary:,}")

# ==========================================================
# Percentage
# ==========================================================

marks = 92.75

print(f"{marks:.1f}%")

# ==========================================================
# format()
# ==========================================================

print("Name : {}".format(name))
print("Age : {}".format(age))

print("{0} is {1} years old.".format(name, age))

# ==========================================================
# % Formatting
# ==========================================================

print("Name : %s" % name)
print("Age : %d" % age)
print("PI : %.2f" % pi)

# ==========================================================
# Alignment
# ==========================================================

print(f"|{'Python':<15}|")
print(f"|{'Python':>15}|")
print(f"|{'Python':^15}|")

# ==========================================================
# Practical Example
# ==========================================================

student = "Rahul"
course = "Python"
marks = 91.35

print("="*40)
print("REPORT CARD")
print("="*40)

print(f"Student : {student}")
print(f"Course  : {course}")
print(f"Marks   : {marks:.2f}%")