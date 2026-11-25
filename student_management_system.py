import json
import os

folder = "student_data"

if not os.path.exists(folder):
    os.makedirs(folder)


students = []

def get_file_name(course):
    return os.path.join(folder, f"{course.upper()}.json")

def load_students(course):
    file_name = get_file_name(course)

    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    else:
        return []

    
def save_students(course, students):
    file_name = get_file_name(course)

    with open(file_name, "w") as f:
        json.dump(students, f, indent=4)


def add_student():
    print("--- Add Student ---")

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    while True:
        print("/n---Student Details---")
        print("Roll Number:", roll_no)
        print("Name:", name)
        print("Age:", age)
        print("Course:", course)
        print("Marks:", marks)

        print("/n1.save student")
        print("2. Edit Information")
        print("3. Cancel")

        choice = input("Enter your choice: ")

        if choice == "1":

            students = load_students(course)

            student = {
                "roll_no": roll_no,
                "name": name,
                "age": age,
                "course": course,
                "marks": marks
            }

            students.append(student)

            
            save_students(course, students)

            print("Student added successfully!")

            break

        elif choice == "2":
            print("/n---Edit Information---")
            print("1. Roll Number")
            print("2. Name")
            print("3. Age")
            print("4. Course")
            print("5. Marks")
            print("6. Done")

            edit_choice = input("Enter your choice: ")

            if edit_choice == "i":
                roll_no = input("Enter New Roll Number: ")
            elif edit_choice == "ii":
                name = input("Enter New Name: ")
            elif edit_choice == "iii":
                age = input("Enter New Age: ")
            elif edit_choice == "iv":
                course = input("Enter New Course: ")
            elif edit_choice == "v":
                marks = input("Enter New Marks: ")
            elif edit_choice == "vi":
                continue
            else:
                print("Invalid choice! Please try again.")

        elif choice == "3":
            print("Student addition canceled.")
            break
        else:
            print("Invalid choice! Please try again.")

def view_students():
    print("--- All Students ---")

    course = input("Enter Course to view students: ")
    students = load_students(course)

    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("Roll Number:", student["roll_no"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            print("\n--------------------\n")


def search_student():
    print("--- Search Student ---")

    roll_no = input("Enter Roll Number: ")
    course = input("Enter Course: ")
    students = load_students(course)

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student Found!")
            print("Roll Number:", student["roll_no"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            print("\n--------------------\n")
            return

    print("Student not found.")


def update_student():
    print("--- Update Student ---")

    roll_no = input("Enter Roll Number: ")
    course = input("Enter Course: ")
    students = load_students(course)

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")
            student["marks"] = input("Enter New Marks: ")

            save_students(course, students)
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("--- Delete Student ---")

    roll_no = input("Enter Roll Number: ")
    course = input("Enter Course: ")
    students = load_students(course)

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(course, students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:

    print("   STUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")