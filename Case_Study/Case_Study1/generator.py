def student_generator(students):
    print("Fetching Student Records...")
    print("--------------------------------")
    for s in students.values():
        yield f"{s.id} - {s.name}"

