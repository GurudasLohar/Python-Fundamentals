# Loops

# For loop
for i in range(10):
    print(i, end=' ')

# Normally, print() moves to a new line after printing.
# print(i, end=' ') => "After printing the value, don't go to the next line. Instead, print a space."    

print()

# While loop
count = 0
while count < 5:
    print(count, end=' ')
    count += 1
print()

# Loop control: break, continue
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)

# continue => "Skip the rest of the code in this iteration and go to the next iteration."
# break => "Exit the loop immediately."   