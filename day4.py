class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = student("Huzaifa", 20)
s1.display()

#############################################
class Employee:
    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Department:", self.department)

e1 = Employee("Joel", 30, 50000, "IT")
e2 = Employee("John", 25, 40000, "HR")

e1.display()
print()
e2.display()

################## Single-Level Inheritance #################
class Person:
    def show_name(self):
        print("My name is Mohammed Huzaifa")

class Student(Person):
    def study(self):
        print("I am studying")

s = Student()
s.show_name()
s.study()

################## Multilevel Inheritance ##################
class Grandfather:
    def house(self):
        print("Grandfather has a house")

class Father(Grandfather):
    def car(self):
        print("Father has a car")

class Son(Father):
    def bike(self):
        print("Son has a bike")

s = Son()
s.house()
s.car()
s.bike()

################### Multiple Inheritance #################
class Teacher:
    def teach(self):
        print("Teacher can teach")

class Writer:
    def write(self):
        print("Writer can write")

class Professor(Teacher, Writer):
    def research(self):
        print("Professor can research")

p = Professor()
p.teach()
p.write()
p.research()

################## Hierarchical Inheritance #################
class Vehicle:
    def start(self):
        print("Vehicle can start")

class Car(Vehicle):
    def drive(self):
        print("Car can drive")

class Bike(Vehicle):
    def ride(self):
        print("Bike can ride")

c = Car()
c.start()
c.drive()

b = Bike()
b.start()
b.ride()

################## Hybrid Inheritance ####################
class Person:
    def name(self):
        print("My name is Ahmed")

class Employee(Person):
    def work(self):
        print("Employee can work")

class Student(Person):
    def study(self):
        print("Student can study")

class Intern(Employee, Student):
    def learn(self):
        print("Intern can learn")

i = Intern()
i.name()
i.work()
i.study()
i.learn()

#################### Abstract Method #######################
from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(vehicle):
    def start(self):
        print("car starts with a key")

class Bike(vehicle):
    def start(self):
        print("Bike starts with a button")

car = Car()
bike = Bike()
car.start()
bike.start()

##################### Polymorphism ######################
class Rectangle:
    def calculate(self):
        print("Area of Rectangle = 50")


class Circle:
    def calculate(self):
        print("Area of Circle = 78.5")


rectangle = Rectangle()
circle = Circle()

rectangle.calculate()
circle.calculate()

###################### Encapsulation ####################
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

students = student("Arun", 90)
print(students.name)
print(students.marks)
students.marks = 500
print(students.marks)

#########################################################
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks.")

student = Student("Joel", 90)
print("Old marks:", student.get_marks())

student.set_marks(80)
print("New marks:", student.get_marks())

###################### Mini Project #####################
from abc import ABC, abstractmethod

# Abstract class
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name

        # Encapsulation
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    @abstractmethod
    def calculate_salary(self):
        pass

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())

# Inheritance
class Developer(Employee):
    def calculate_salary(self):
        # Developer gets 10% bonus
        bonus = self.get_salary() * 0.10
        return self.get_salary() + bonus

# Inheritance
class Manager(Employee):
    def calculate_salary(self):
        # Manager gets 20% bonus
        bonus = self.get_salary() * 0.20
        return self.get_salary() + bonus

# Objects
developer = Developer("Rahul", 30000)
manager = Manager("Priya", 50000)

# Polymorphism
developer.display()
print()
manager.display()