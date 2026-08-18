name = "Mohammed Huzaifa"

def student():
    print(name)
student()

# ##############################################
print(name)

def student():
    age =27
    print(age)
student()

########################## Global + Local scope ##########################
name = "Joel"

def display():
    age = 20
    print(age)
    print(name)
display()

################################################
name = "Vikash"
def display():
    name = "Harsha"
    print(name)
display()
print(name)

################################################
name = "Arun"
name = "Joel"
def display():
    name = "CS"
    name = "DS"
    print(name)
display()
print(name)

################################################
square = lambda x: x * x
print(square(5))

################################################
large = lambda x, y: x if x > y else y
print(large(10, 20))

################################################
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)

################################################
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(6))

################################################
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b -1)
print(power(2, 4))