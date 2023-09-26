def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Define a Student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test the function with a list of student objects
students = [
    Student("Madhumitha", "2226jb26", 3.9),
    Student("Harini", "2226jb16", 3.7),
    Student("Sangeerthana", "2226jb40", 4.0),
    Student("Nandhana", "2226jb28", 3.5)
]

sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")