import json

def load_student():
    try:
        with open("student.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def add_student(student_details):


    num = int(input("How many student you want to add:"))

    for i in range(num):
        roll_no = input(f"enter the roll no of studenet {i+1}:")
        name = input("enter the name of student:")
        age = int(input("enter the age of student:"))
        course = input("enter the coure:")
        phone_no = input("enter the valid phone number:")
        mail = input("enter your mail:")
        address = input("enter your address:")
        print("\n")

    
        student = {
            "Roll No": roll_no,
            "Name": name,
            "Age": age,
            "Course": course,
            "Phone": phone_no,
            "Email": mail,
            "Address": address
        }
    
        student_details.append(student)
    print("\nStudents added successfully\n")
    return student
def view_student(student_details):
    if len(student_details) == 0:
        print("\nNo student records found.\n")
        return
    for student in student_details:
        print(f"Roll No : {student['Roll No']}")
        print(f"Name    : {student['Name']}")
        print(f"Age     : {student['Age']}")
        print(f"Course  : {student['Course']}")
        print(f"Phone   : {student['Phone']}")
        print(f"Email   : {student['Email']}")
        print(f"Address : {student['Address']}")
        print("-" * 30)

def update_student(student_details):

    roll_no = input("Enter Roll Number: ")

    print('''1. Update Name
            2. Update Age
            3. Update Course
            4. Update Phone
            5. Update Email
            6. Update Address''')

    for student in student_details:
        

        if student['Roll No'] == roll_no:

            choice = int(input("Enter your choice: "))

            if choice == 1:
                student["Name"] = input("Enter new name: ")

            elif choice == 2:
                student["Age"] = int(input("Enter new age: "))

            elif choice == 3:
                student["Course"] = input("Enter new course: ")

            elif choice == 4:
                student["Phone"] = input("Enter new phone: ")

            elif choice == 5:
                student["Email"] = input("Enter new email: ")

            elif choice == 6:
                student["Address"] = input("Enter new address: ")

            print("Student updated successfully.")
            return

    print("Student not found.")

def delete_student(student_details):

    roll_no = input("enter the roll no or name which you delete :")

    for student in student_details:
        if student['Roll No'] == roll_no:
            student_details.remove(student)
            print("student deleted successfully")
            return

    print("student not found")

def search_student(student_details):

    value = input("Enter Roll Number or Name to search: ")

    for student in student_details:

        if str(student["Roll No"]) == value or student["Name"].lower() == value.lower():
            print(student)
            return

    print("Student not found")

def sort_student(student_details):
    student_details.sort(key = lambda student:student["Roll No"])

    print("student sorted successfully")


def save_student(student_details):
    with open("student.json", "w") as file:
        json.dump(student_details, file, indent = 4)

    print("data saved successfully.")

student_details = load_student()



while True:
    print('''
choose
1. press 1 for add student
2. press 2 for view studdent
3. press 3 for update student
4. press 4 for delete student
5. press 5 for search student
6. press 6 for sort student
7. press 7 for exit''')
    choice = int(input("enter your choice :"))
    print("\n")

    if choice == 1:
        add_student(student_details)
        save_student(student_details)
    elif choice == 2:
        view_student(student_details)
    elif choice == 3:
        update_student(student_details)
        save_student(student_details)
    elif choice == 4:
        delete_student(student_details)
        save_student(student_details)
    elif choice == 5:
        search_student(student_details)
    elif choice == 6:
        sort_student(student_details)
        save_student(student_details)
    elif choice == 7:
        print("thank you")
        break
    else:
        print("invalid choice")