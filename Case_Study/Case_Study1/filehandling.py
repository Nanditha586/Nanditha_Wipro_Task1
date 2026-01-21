import json
import csv
from decorators import admin_only
@admin_only
def save_students_json(students):
    data = []
    for s in students.values():
        data.append({
            "id": s.id,
            "name": s.name,
            "department": s.department.name,
            "semester": s.semester,
            "marks": s.marks
        })
    with open("students.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Student data successfully saved to students.json")

@admin_only
def generate_csv_report(students):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in students.values():
            avg = sum(s.marks)/len(s.marks)
            grade = s.calculate_grades(avg)
            writer.writerow([s.id, s.name, s.department.name, round(avg,1), grade])
    print("CSV Report (students_report.csv) generated")

