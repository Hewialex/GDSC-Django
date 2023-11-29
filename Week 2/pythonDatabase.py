student_database = {}

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    student_database[name] = {"Age": age, "Grade": grade}
    print(f"{name} added to the database.")

def view_student():
    name = input("Enter student name to view details: ")
    if name in student_database:
        print(f"\nStudent Details:\nName: {name}\nAge: {student_database[name]['Age']}\nGrade: {student_database[name]['Grade']}")
    else:
        print(f"Student with the name {name} not found in the database.")

def list_all_students():
    print("\nList of All Students:")
    for name, details in student_database.items():
        print(f"Name: {name}, Age: {details['Age']}, Grade: {details['Grade']}")

def update_student():
    name = input("Enter student name to update details: ")
    if name in student_database:
        print(f"\nUpdating details for {name}:")
        age = int(input("Enter new age (press Enter to keep current age): ") or student_database[name]['Age'])
        grade = input("Enter new grade (press Enter to keep current grade): ") or student_database[name]['Grade']
        student_database[name]['Age'] = age
        student_database[name]['Grade'] = grade
        print(f"Details for {name} updated.")
    else:
        print(f"Student with the name {name} not found in the database.")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in student_database:
        del student_database[name]
        print(f"{name} deleted from the database.")
    else:
        print(f"Student with the name {name} not found in the database.")

while True:
    print("\nStudent Database Menu:")
    print("1. Add Student")
    print("2. View Student Details")
    print("3. List All Students")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        list_all_students()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
