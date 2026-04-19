#Problem Statment
"Class and Object Problem Statement : "
"Create a class named Student with attributes "
"such as student name, roll number, and marks of"
" subject. The class should have functions to "
"accept student details, display the information,"
"and calculate the total and average marks. "
"Create objects of the class and use the functions"
"to perform these operations."
#solution
'''class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.maths = 0
        self.physics = 0
        self.chemistry = 0

    def accept(self):
        self.name = input("Enter student name: ")
        self.roll_no = int(input("Enter roll number: "))
        self.maths = int(input("Enter Maths marks: "))
        self.physics = int(input("Enter Physics marks: "))
        self.chemistry = int(input("Enter Chemistry marks: "))

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Maths:", self.maths)
        print("Physics:", self.physics)
        print("Chemistry:", self.chemistry)

    def total_marks(self):
        return self.maths + self.physics + self.chemistry

    def average_marks(self):
        return self.total_marks() / 3


# Creating object
s1 = Student()
s1.accept()
s1.display()

print("Total Marks:", s1.total_marks())
print("Average Marks:", s1.average_marks())'''

#inheritance

#Class example
'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, marks):
        Person.__init__(self, name, age)
        self.marks = marks

    def stud(self):
        print("I am stud")


student1 = Student("abc", 18, 43)

student1.display()
student1.stud()
student1.marks = 91'''

