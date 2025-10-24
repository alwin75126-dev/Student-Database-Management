import json
import os

db_file = "students.json"

def load_data():
    if os.path.exists(db_file):
        with open(db_file, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(db_file, 'w') as f:
        json.dump(data, f, indent=4)

def menu():
    print("\nStudentDB Management System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")
    return input("Choose an option: ")

def add_student():
    data = load_data()
    student = {
        "id": input("Enter student ID: "),
        "name": input("Enter name: "),
        "age": input("Enter age: "),
        "grade": input("Enter grade: ")
    }
    data.append(student)
    save_data(data)
    print("Student added successfully.")

def view_students():
    data = load_data()
    if not data:
        print("No students found.")
        return
    for s in data:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")

def update_student():
    data = load_data()
    sid = input("Enter student ID to update: ")
    for s in data:
        if s["id"] == sid:
            s["name"] = input(f"Enter new name ({s['name']}): ") or s['name']
            s["age"] = input(f"Enter new age ({s['age']}): ") or s['age']
            s["grade"] = input(f"Enter new grade ({s['grade']}): ") or s['grade']
            save_data(data)
            print("Student updated.")
            return
    print("Student ID not found.")

def delete_student():
    data = load_data()
    sid = input("Enter student ID to delete: ")
    new_data = [s for s in data if s["id"] != sid]
    if len(new_data) == len(data):
        print("Student ID not found.")
        return
    save_data(new_data)
    print("Student deleted successfully.")

def search_student():
    data = load_data()
    sid = input("Enter student ID to search: ")
    for s in data:
        if s["id"] == sid:
            print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")
            return
    print("Student ID not found.")

while True:
    choice = menu()
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        search_student()
    elif choice == '6':
        break
    else:
        print("Invalid choice.")
