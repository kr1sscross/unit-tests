import csv

# Import from CSV file
def import_students_csv(file_path):
    students = []
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                students.append({'name': row[0], 'present': False})
    except FileNotFoundError:
        print(f"File {file_path} is not found.")
    return students

# Export student attendance list to CSV
def export_students_csv(students, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Present'])
        for student in students:
            writer.writerow([student['name'], student['present']])

# Import student attendace list to TXT
def import_students_txt(file_path):
    students = []
    try:
        with open(file_path, mode='r') as file:
            for line in file:
                name = line.strip()
                students.append({'name': name, 'present': False})
    except FileNotFoundError:
        print(f"File {file_path} is not found.")
    return students

# Export student attendace list to TXT
def export_students_txt(students, file_path):
    with open(file_path, mode='w') as file:
        for student in students:
            file.write(f"{student['name']}: {'Present' if student['present'] else 'Absent'}\n")

# Check attendance
def mark_attendance(students):
    for student in students:
        present = input(f"Czy {student['name']} is present? (y/n): ").strip().lower()
        student['present'] = present == 'y'
