from decorators import performance_time,log_execution
from descriptors import Validate_Marks, Salary_Access
from decorators import admin_only
from abc import ABC,abstractmethod
#Department Class
class Department:
    def __init__(self, dept_id, name):
        self.dept_id = dept_id
        self.name = name
        self.students = []
        self.faculty = []
        self.courses = []
    def add_student(self, student):
        self.students.append(student)
    def add_faculty(self, faculty):
        self.faculty.append(faculty)
    def add_course(self, course):
        self.courses.append(course)
#Person Class
class Person(ABC):
    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department
    @abstractmethod
    def get_details(self):
        pass
    def __del__(self):
        print(f"Cleaning up resources for {self.name}")
#Student Class
class Student(Person):
    marks = Validate_Marks()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []
        department.add_student(self)
    # Polymorphism
    def get_details(self):
        print("Student Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Student")
        print(f"Department: {self.department.name}")
    # Parameterized method
    def enroll_student(self, course):
        self.courses.append(course)
        print("Enrollment Successful")
        print("--------------------------------")
        print(f"Student Name : {self.name}")
        print(f"Course       : {course.name}")
    # Parameterized method
    def calculate_grades(self, avg):
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        else:
            return "C"
    @log_execution
    @performance_time
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = self.calculate_grades(avg)
        print("Student Performance Report")
        print("--------------------------------")
        print(f"Student Name : {self.name}")
        print(f"Marks        : {self.marks}")
        print(f"Average      : {round(avg,1)}")
        print(f"Grade        : {grade}")
        return avg
    # Operator overloading
    def __gt__(self, other):
        return self.calculate_performance() > other.calculate_performance()
#faculty Class
class Faculty(Person):
    salary = Salary_Access()
    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary
        department.add_faculty(self)
    # Polymorphism
    def get_details(self):
        print("Faculty Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Faculty")
        print(f"Department: {self.department.name}")
#Course Class
class Course:
    def __init__(self, code, name, credits, department):
        self.code = code
        self.name = name
        self.credits = credits
        self.department = department
        self.faculty = None
        department.add_course(self)
    # Parameterized method
    def assign_faculty(self, faculty):
        self.faculty = faculty
        print("Faculty Assigned Successfully")
        print("--------------------------------")
        print(f"Course  : {self.name}")
        print(f"Faculty : {faculty.name}")
    # Operator overloading
    def __add__(self, other):
        return self.credits + other.credits