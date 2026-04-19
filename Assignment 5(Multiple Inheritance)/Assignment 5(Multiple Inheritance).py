#Inheritance Problem Statement : 
#Create python program to show how the Manager 
#class inherits attributes and methods from both
#Person and Employee, and how we can add additional 
# behaviors and properties in the Manager class.
#Person Class: Contains common attributes like name and age.
#Employee Class: Inherits from Person and adds specific 
#attributes such as employee_id and salary.
#Manager Class: Inherits from both Person and Employee,
#adding its own specific attribute department
#and combining behaviors from both parent classes.



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)   
        self.employee_id = employee_id
        self.salary = salary

    def show_employee(self):
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def show_manager(self):
        print(f"Department: {self.department}")

    def full_details(self):
        self.show_person()
        self.show_employee()
        self.show_manager()

m1 = Manager("Atharva", 21, "EMP101", 80000, "IT")

m1.full_details()

