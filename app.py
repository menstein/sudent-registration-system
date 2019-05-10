### Student Registration System ###
-----------------------------------
# This simple system about registration is to ilustrate about constructing a dictionary from the set.
# The user of this app would be an Administration Staff of some school institution for storing data about student and their marks.
# The step would be input a student's name which then the system would generate an ID for the student,
# and then the user has to input the student's marks on certain subject (but subject is not define yet in this case),
# and with those data, the system then could generate basic information for each student and make a list of that when we need it.
-----------------------------------
#The step would be defining all of the method needed for the system to works, then making a menu to access it.

student_list = []

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = []
        
    def average_mark(self):
        number = len(student.marks)
            if number == 0:
            return 0
        total = sum(student.marks)
        return total / number

def create_student():
    name = input("input the student's name: ")
    student_data = Student(name)
    return student_data

def add_mark(student,mark):
    student.marks.append(mark)

def print_student_details(student):
    print("{}'s average mark: {}".format(student.name,
                                         student.average_mark()))

def print_student_list(students): #to list down all of the inputted student with the information details.
    for i,student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)

def menu():
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to add  a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the mark to be added: "))
            add_mark(student,new_mark)
        selection = input("Enter 'p' to print the student list, "
                          "'s' to add a new student, "
                          "'a' to add  a mark to a student, "
                          "or 'q' to quit. "
                          "Enter your selection: ")

menu()
