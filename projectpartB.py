#Gavin Cartwright
#March 28th 2023
#Project Part B (Student Management)
###############################################################
import csv 

#Fields include: Age, Grade, Name
with open('students.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
###############################################################
#Classes
#Person Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Student class inheritance from person class
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        
    def display_info(self):
        print(f"{self.name}, {self.age}, {self.grade}")

class StudentList(list):
    def __init__(self, students=None):
        super().__init__(students or [])

    def add_student(self, student):
        self.append(student)

    def add_student_to_csv(self, file_path, student):
        with open(file_path, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([student.name, student.age, student.grade])
        self.add_student(student)
        
    def remove_student(self, name):
        for i in range(len(self)):
            if self[i].name == name:
                removed_student = self.pop(i)
                return removed_student
        return None

class GradeList(StudentList):
    def remove_student(self, name):
        removed_student = super().remove_student(name)
        if removed_student is not None:
            with open('students.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)
            with open('students.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for row in rows:
                    if row[0] != removed_student.name:
                        writer.writerow(row)
            return True
        return False

###############################################################
#Functions
#CSV file contains name, age, and grade
def read_students_csv(file_path):
    students = GradeList()
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            name, age_str, grade_str = [field.strip() for field in row]
            age = int(age_str)
            grade = int(grade_str)
            student = Student(name, age, grade)
            students.add_student(student)
    return students

#Student finder function
def find_student(students, name):
    for student in students:
        if student.name == name:
            return student
    return None

#Creates the ability to remove students from the list
def remove_student_from_csv(file_path, name):
    students = read_students_csv(file_path)
    removed_student = students.remove_student(name)
    if removed_student is not None:
        print(f"{name} has been removed from the list.")
    else:
        print(f"{name} was not found in the list.")


#Adds a student to the list of students
def add():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = int(input("Enter student grade: "))

    student = Student(name, age, grade)
    student_list = StudentList()

    file_path = 'students.csv'
    student_list.add_student_to_csv(file_path, student)

    print(f"Student {name} added successfully!")

#Removes a student from the list of students
def remove():
    name = input('Enter name of student you wish to remove: ')
    remove_student_from_csv('students.csv', name)

#Shows the active list of students
def student_list():
    students = read_students_csv('students.csv')
    for student in students:
        student.display_info()

#Shows the grade of a selected student
def grades():
    students = read_students_csv('students.csv')
    name = input('Enter name of student you wish to find: ')
    student = find_student(students, name)
    if student:
        student.display_info()
    else: 
        print('Student not Found')