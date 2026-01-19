
from classes import Department, Student, Faculty, Course
from filehandling import save_students_json,generate_csv_report
from generator import student_generator
departments = {}
students = {}
faculty = {}
courses = {}

while True:
    print("\n1 Add Student")
    print("2 Add Faculty")
    print("3 Add Course")
    print("4 Enroll Student to Course")
    print("5 Calculate Student Performance")
    print("6 Compare Two Students")
    print("7 Generate Reports")
    print("8 Student Generator")
    print("9 Faculty Details")
    print("10 Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            sid = input("Student ID: ")
            if sid in students:
               raise Exception("Student ID already exists")
            name = input("Name: ")
            dept = input("Department: ")
            sem = int(input("Semester: "))
            marks = list(map(int, input("Enter marks: ").split()))

            if dept not in departments:
                departments[dept] = Department("D"+str(len(departments)+1), dept)

            students[sid] = Student(sid, name, departments[dept], sem, marks)
            print("Student Created Successfully")

        elif choice == "2":
            fid = input("Faculty ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            sal = int(input("Salary: "))

            if dept not in departments:
                departments[dept] = Department("D"+str(len(departments)+1), dept)

            faculty[fid] = Faculty(fid, name, departments[dept], sal)
            print("Faculty Created Successfully")

        elif choice == "3":
            code = input("Course Code: ")
            name = input("Course Name: ")
            credits = int(input("Credits: "))
            dept = input("Department: ")

            course = Course(code, name, credits, departments[dept])
            courses[code] = course

            fid = input("Faculty ID: ")
            course.assign_faculty(faculty[fid])
            print("Course Added Successfully")

        elif choice == "4":
            sid = input("Student ID: ")
            code = input("Course Code: ")
            students[sid].enroll_student(courses[code])

        elif choice == "5":
            sid = input("Student ID: ")
            students[sid].calculate_performance()

        elif choice == "6":
            s1 = students[input("Student 1 ID: ")]
            s2 = students[input("Student 2 ID: ")]
            print(f"{s1.name} > {s2.name} : {s1 > s2}")

        elif choice == "7":
            generate_csv_report(students)
            save_students_json(students)

        elif choice == "8":
            for record in student_generator(students):
                print(record)

        elif choice == "9":
            print("Thank you for using Smart University Management System")
            break



    except ValueError as ve:
        print("Invalid Marks")
        print("Error:", ve)
    except PermissionError as pe:
        print(pe)
    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print("Error:", e)









