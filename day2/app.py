rollno = 101
cgpa = 8.5
pass_status = True
name = input("Enter your name: ")

print("Roll No:", rollno)
print("CGPA:", cgpa)
print("Pass Status:", pass_status)
print("Name:", name)

##################################################
name = input("Enter your name: ")
Rollno = input("Enter your roll number: ")
college = input("Enter your college name: ")
cgpa = input("Enter your CGPA: ")

print("Welcome to RIT", name)
print("Your roll number is", Rollno)
print("You are studying at", college)
print("Your CGPA is", cgpa)

##################################################
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

# Arithmetic operators
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Comparison operators
print(a == b)
print(a != b)
print(a > b)
print(a < b)

# Check whether a is even
print(a % 2 == 0)

#################################################
age = 20

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
##################################################
Positive, Negative or Zero
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

###################################################
# PIN Verification
correct_pin = "1234"

pin = input("Enter your PIN: ")

if pin == correct_pin:
    print("Login successful.")
    print("Welcome to RIT Bank")
else:
    print("Incorrect PIN.")
    print("Please try again")

#################################################
for i in range(3):
    for j in range(5):
        print("*", end="")
    print()

#################################################
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

#################################################
def greet(name):
    print("Hello, " + name + "! Welcome to RIT.")

greet("Huzaifa")