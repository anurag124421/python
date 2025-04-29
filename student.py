# Initialize an empty dictionary for student records
student_records = {}

# Function to add a new student record
def add_student(student_id, name, grade, attendance):
    student_records[student_id] = {'Name': name, 'Grade': grade, 'Attendance': attendance}
    print(f"Added student {name} with ID {student_id}.")

# Function to update a student's grade or attendance
def update_student(student_id, grade=None, attendance=None):
    if student_id in student_records:
        if grade is not None:
            student_records[student_id]['Grade'] = grade
        if attendance is not None:
            student_records[student_id]['Attendance'] = attendance
        print(f"Updated record for student ID {student_id}.")
    else:
        print(f"Student ID {student_id} not found!")

# Function to delete a student record
def delete_student(student_id):
    if student_id in student_records:
        del student_records[student_id]
        print(f"Deleted record for student ID {student_id}.")
    else:
        print(f"Student ID {student_id} not found!")

# Function to display all student records
def display_records():
    if student_records:
        for student_id, details in student_records.items():
            print(f"ID: {student_id}, Name: {details['Name']}, Grade: {details['Grade']}, Attendance: {details['Attendance']}")
    else:
        print("No records to display!")

# Sample user interaction
add_student(101, "Alice", "A", 95)
add_student(102, "Bob", "B", 85)
update_student(101, grade="A+", attendance=98)
delete_student(102)
display_records()