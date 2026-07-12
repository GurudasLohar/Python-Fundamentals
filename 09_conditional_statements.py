# Conditional Statements

age = 80

if age < 18:
    print("Minor")
elif age >= 18 and age < 65:
    print("Adult")
else:
    print("Senior")

# Ternary operator
status = "Eligible" if age >= 18 else "Not Eligible"
print(status)