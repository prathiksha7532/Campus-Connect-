import sqlite3

conn = sqlite3.connect("campusconnect.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    year INTEGER,
    email TEXT,
    phone TEXT,
    attendance REAL,
    cgpa REAL
)
""")
conn.commit()

def get_status(cgpa):
    if cgpa >= 8.5:
        return "Excellent"
    elif cgpa >= 7.0:
        return "Good"
    elif cgpa >= 5.0:
        return "Average"
    return "Needs Improvement"

def add_student():
    student_id = int(input("Student ID: "))
    name = input("Name: ")
    department = input("Department: ")
    year = int(input("Year: "))
    email = input("Email: ")
    phone = input("Phone: ")
    attendance = float(input("Attendance (%): "))
    cgpa = float(input("CGPA: "))

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (student_id, name, department, year, email, phone, attendance, cgpa)
    )
    conn.commit()
    print("Student Added Successfully")

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row, "| Performance:", get_status(row[7]))

def search_student():
    sid = int(input("Enter Student ID: "))
    cursor.execute("SELECT * FROM students WHERE student_id=?", (sid,))
    print(cursor.fetchone())

def update_student():
    sid = int(input("Enter Student ID: "))
    name = input("New Name: ")
    cursor.execute("UPDATE students SET name=? WHERE student_id=?", (name, sid))
    conn.commit()
    print("Updated Successfully")

def delete_student():
    sid = int(input("Enter Student ID: "))
    cursor.execute("DELETE FROM students WHERE student_id=?", (sid,))
    conn.commit()
    print("Deleted Successfully")

while True:
    print("\\n=== CAMPUSCONNECT ===")
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Exit")

    choice = input("Enter Choice: ")

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
        break
    else:
        print("Invalid Choice")

conn.close()
